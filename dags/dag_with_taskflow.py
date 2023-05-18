'''
 # @ Author: Your name
 # @ Create Time: 2023-05-17 10:46:48
 # @ Modified by: Your name
 # @ Modified time: 2023-05-17 10:52:47
 # @ Description: Since Airflow 2.0, it provides a TaskFlow API 
 that makes writing pipeline easier and cleaner.
 
 https://airflow.apache.org/docs/apache-airflow/stable/tutorial/taskflow.html
 
 This script is dedicated to understand taskflow api. 
 It kinda works like flask now with decorator for callback.
'''



from airflow.decorators import dag, task
from datetime import datetime,timedelta


default_args = {
    "owner": "adamzhang",
    "retries": 5,
    "retry_delay": timedelta(minutes=5)
}



@dag(
    dag_id = "dag_with_taskflow_api_v02",
    default_args = default_args,
    start_date = datetime(2023,5,15),
    catchup = False,
    schedule='@daily'
)
def hello_world_etl():
    """
    definition of the dag with TaskFlow API, it consists
    of three tasks defined with just a python function.
    Before TaskFlow:
        task = python function + task
    Example pseudo-code:
        def get_name(ti):
            ti.xcom_push(key = 'first_name',value = 'Jerry')
            ti.xcom_push(key = 'last_name',value = 'Zhang')

        + 
        
        task2 = PythonOperator(
        task_id = 'get_name',
        python_callable = get_name
        )
        
    After TaskFlow:
        task = python function + decorator
        
        @task()
        def get_name():
            return blabla
    """
    @task(multiple_outputs = True)
    def get_name():
        return {"first_name" : "Jerry",
                "last_name": "The brick"}
    
    @task()
    def get_age():
        return "30"
    
    @task()
    def greet(first_name,last_name, age):
        print(f"Hello Airflow! My name is {first_name} {last_name}"
              f" and I am {age} years old!")
        
    name_dict = get_name()
    
    age = get_age() 
    
    greet(first_name = name_dict['first_name'], 
          last_name = name_dict['last_name'], 
          age=age)

# create an instance of our dag
greet_dag = hello_world_etl()

