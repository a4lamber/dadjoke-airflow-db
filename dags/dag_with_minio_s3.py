'''
 # @ Author: Your name
 # @ Create Time: 2023-05-19 09:31:24
 # @ Modified by: Your name
 # @ Modified time: 2023-05-19 09:31:39
 # @ Description: connect airflow with minio server (s3-like bucket).
 We will practice:
 - how to spin up a minio server with docker
 - how to connect airflow with minio (for prep with s3)
 - pick up on how to use sensor operator to sense the arrival of data
 in a bucket 
 '''
 
from datetime import datetime, timedelta
 
from airflow import DAG
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
from airflow import dag_processing


default_args = {
    "owner": "adamzhang",
    "retries": 5,
    "retry_delay": timedelta(minutes=5)
}


with DAG(
    default_args = default_args,
    dag_id = "dag_with_minio_s3_v04",
    schedule = '@daily',
    start_date =datetime(2023,5,18)
) as dag:
    #
    task1 = S3KeySensor(
        task_id='sensor_minio_s3',
        bucket_name='airflow',
        bucket_key='fielddata.csv',
        aws_conn_id = 'minio_conn'
    )