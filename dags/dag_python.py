'''
 # @ Author: Adam Zhang
 # @ Create Time: 2023-05-16 16:12:45
 # @ Modified by: Adam Zhang
 # @ Modified time: 2023-05-17 10:30:48
 # @ Description: pick up airflow with python operator
 and it is designed to communicate within the DAG (max 64 kb).
 Please read more in the following doc
 https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/xcoms.html
 '''


from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime,timedelta



default_args = {
    "owner": "adamzhang",
    "retries": 5,
    "retry_delay": timedelta(minutes=5)
}

def get_name(ti):
    ti.xcom_push(key = 'first_name',value = 'Jerry')
    ti.xcom_push(key = 'last_name',value = 'Zhang')

def get_age(ti):
    ti.xcom_push(key = 'age', value = 30)

def greet(ti):
    first_name = ti.xcom_pull(task_ids = 'get_name',key = 'first_name')
    last_name = ti.xcom_pull(task_ids = 'get_name',key = 'last_name')
    age = ti.xcom_pull(task_ids = 'get_age',key = 'age')

    print(f"Hello World my name is {first_name} {last_name},"
          f"my age is {age}")


with DAG(
    default_args = default_args,
    dag_id = "our_dag_with_python_operator_v03",
    description = "our first dag using python operator",
    start_date = datetime(2023,5,17),
    schedule_interval = '@daily'
    
) as dag:
    
    
    task1 = PythonOperator(
        task_id = 'greet',
        python_callable = greet,
    )
    
    task2 = PythonOperator(
        task_id = 'get_name',
        python_callable = get_name
    )
    
    task3 = PythonOperator(
        task_id = "get_age",
        python_callable = get_age
    )
    
    [task2, task3] >> task1