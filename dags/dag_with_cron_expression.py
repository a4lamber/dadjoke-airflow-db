'''
 # @ Author: Yixiang Zhang
 # @ Create Time: 2023-05-17 13:16:14
 # @ Modified by: Yixiang Zhang
 # @ Modified time: 2023-05-17 13:18:14
 # @ Description: use crontab guru for double check
 https://crontab.guru/
 '''


from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "adamzhang",
    "retries": 5,
    "retry_delay": timedelta(minutes=5)
}


with DAG(
    dag_id = "dag_with_cronnn_v03",
    default_args = default_args,
    description="this dag is to learn cron",
    start_date = datetime(2023,5,1),
    schedule ="0 0 * * *",
    catchup = False,
) as dag:
    # define a task in a dag
    task1 = BashOperator(
        task_id = 'task1',
        bash_command = "echo dag with cron!"
    )     

    