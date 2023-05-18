'''
 # @ Author: Adam Zhang
 # @ Create Time: 2023-05-16 16:32:04
 # @ Modified by: Adam Zhang
 # @ Modified time: 2023-05-16 16:32:46
 # @ Description: send out daily dad joke to me
 '''

from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'adamzhang',
    'retries': 5,
    'retry_dealy':timedelta(minutes=2)
}


with DAG(
    dag_id= "dad_joke",
    default_args = default_args,
    description= "this is our first dag we write",
    start_date = datetime(2023,5,16),
    schedule_interval = '@daily'
    
) as dag:
    
    # task1: fetch a random dad joke
    task1 = BashOperator(
        task_id = 'fetch_random_dad_joke',
        bash_command = 'curl -H "Accept: text/plain" https://icanhazdadjoke.com/'
    )
    


