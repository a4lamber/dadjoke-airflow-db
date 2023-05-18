'''
 # @ Author: Yixiang Zhang
 # @ Create Time: 2023-05-16 15:23:22
 # @ Modified by: Yixiang Zhang
 # @ Modified time: 2023-05-16 16:14:55
 # @ Description: learning our first airflow DAG with bash operator.
'''


from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime,timedelta


default_args = {
    'owner': 'adamzhang',
    'retries': 5,
    'retry_dealy':timedelta(minutes=2)
}

with DAG (
    dag_id= "our_first_dag_v3",
    default_args = default_args,
    description= "this is our first dag we write",
    start_date = datetime(2023,5,16),
    schedule_interval = '@daily'
) as dag:
    # set up our first node
    task1 = BashOperator(
        task_id = 'first_task',
        bash_command = "echo hello dag"
    )
    
    task2 = BashOperator(
        task_id = 'second_task',
        bash_command = "sleep 5"
    )
    
    task3 = BashOperator(
        task_id = 'third_task',
        bash_command = "date"
    )
    
    
    # set up dependency
    # task1.set_downstream(task2)
    # task2.set_downstream(task3)
    
    # with bitshift operator
    task1 >> task2
    task2 >> task3