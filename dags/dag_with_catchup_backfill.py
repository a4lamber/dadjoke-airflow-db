'''
 # @ Author: Yixiang Zhang
 # @ Create Time: 2023-05-17 11:40:03
 # @ Modified by: Yixiang Zhang
 # @ Modified time: 2023-05-17 11:47:22
 # @ Description:  learn how to work with cathc-up (argument for DAG)
 and backfill.
 
 For backfill:
 1. go into your scheduler container terminal with 
    docker container exec -it <scheduler-hash-code> bash
 3. see the list of dags
    airflow dags list 
 2. run the following command
    airflow dags backfill -s 2023-04-01 -e 2023-04-10 <dag_name>
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
    dag_id = "dag_with_catchup_backfill_v02",
    default_args = default_args,
    description="this dag is to learn catchup and backfill",
    start_date = datetime(2023,5,1),
    schedule ="@daily",
    catchup = False
) as dag:
    # define a task in a dag
    task1 = BashOperator(
        task_id = 'task1',
        bash_command = "echo this is a simple bash command"
    )     

    task1