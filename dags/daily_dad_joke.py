'''
 # @ Author: Adam Zhang
 # @ Create Time: 2023-05-16 16:32:04
 # @ Modified by: Adam Zhang
 # @ Modified time: 2023-05-16 16:32:46
 # @ Description: This script curl a random joke from
 API and sends it to you everyday.
 '''
import os
import sys

# add root directory of yieldmate to Python path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator

import vault.email_list 

default_args = {
    'owner': 'adamzhang',
    'retries': 5,
    'retry_dealy':timedelta(minutes=2),
    'email': ['adamairflow@outlook.com'],
    'email_on_failure': True,
    'email_on_retry': False,
}


with DAG(
    dag_id= "dad_joke_v_production",
    default_args = default_args,
    description= "this sends u dad joke every weekday at 9",
    start_date = datetime(2023,5,23),
    schedule = '0 9 * * MON-FRI',
    catchup=False
) as dag:
    
    # task1: fetch a random dad joke
    task1 = BashOperator(
        task_id = 'fetch_random_dad_joke',
        bash_command = 'curl -H "Accept: text/plain" https://icanhazdadjoke.com/'
    )
    
    task2 = BashOperator(
        task_id = "echo_joke",
        bash_command="echo {{task_instance.xcom_pull(task_ids=\"fetch_random_dad_joke\")}}"
    )
    
    
    email_html = """
        <div style="font-family: Arial; font-size: 16px;">
        <p>Dear Friends,</p>

        <p>I hope this email finds you well. I am reaching out to you to provide you with today's dad joke. Hope this may cheer you up. </p>

        <p>{{task_instance.xcom_pull(task_ids=\"fetch_random_dad_joke\")}}</p>

        <p>Best regards,</p>

        <p>Adam</p>
        </div>
    """
    
    task3 = EmailOperator(
        task_id = "send_email",
        subject = "Daily GIS Digest",
        to = vault.email_list.receipent,
        # html_content="Date: {{ ds }}"
        html_content= email_html
    )
    
    
    
    task1 >> task2
    task2 >> task3


