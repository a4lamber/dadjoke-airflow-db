'''
 # @ Author: Adam Zhang
 # @ Create Time: 2023-05-16 16:32:04
 # @ Modified by: Adam Zhang
 # @ Modified time: 2023-05-16 16:32:46
 # @ Description: This script curl a random joke from
 API and sends it to you everyday.
 '''

from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator

default_args = {
    'owner': 'adamzhang',
    'retries': 5,
    'retry_dealy':timedelta(minutes=2),
    'email': ['airflowadamzhang@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
}


with DAG(
    dag_id= "dad_joke_v17",
    default_args = default_args,
    description= "this sends u dad joke every day",
    start_date = datetime(2023,5,19),
    schedule = '@daily'
    
) as dag:
    
    # task1: fetch a random dad joke
    task1 = BashOperator(
        task_id = 'fetch_random_dad_joke',
        bash_command = 'curl -H "Accept: text/plain" https://icanhazdadjoke.com/'
    )
    
    # task2 = BashOperator(
    #     task_id = "echo_joke",
    #     bash_command="echo {{task_instance.xcom_pull(task_ids=\"fetch_random_dad_joke\")}}"
    # )
    
    task3 = EmailOperator(
        task_id = "send_email",
        subject = "airflow success alert",
        to = "adamhimy19@gmail.com",
        html_content="Date: {{ ds }}"
    )
    
    task1 >> task3


