'''
 # @ Author: Yixiang Zhang
 # @ Create Time: 2023-05-17 13:36:51
 # @ Modified by: Yixiang Zhang
 # @ Modified time: 2023-05-17 13:55:19
 # @ Description:
 airflow macros documentation
    https://airflow.apache.org/docs/apache-airflow/1.10.5/macros.html
 '''



from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    "owner": "adamzhang",
    "retries": 5,
    "retry_delay": timedelta(minutes=5)
}

with DAG(
    dag_id = "dag_with_postgres_operator_v11",
    default_args = default_args,
    description="this dag is to learn set up with postgres",
    start_date = datetime(2023,5,17),
    schedule ="0 0 * * *",
    catchup = False,
) as dag:
    # define a task in a dag
    task1 = PostgresOperator(
        task_id = "create_postgres_table",
        postgres_conn_id = "postgres_localhost",
        sql = """
            create table if not exists customer (
        first_name VARCHAR(30) not null,
        last_name VARCHAR(30) not null,
        email VARCHAR(60) not null,
        company VARCHAR(60) not null,
        street VARCHAR(50) not null,
        city VARCHAR(30) not null,
        state CHAR(2) not null,
        zip SMALLINT not null,
        phone VARCHAR(20) not null,
        birth_date DATE null,
        sex CHAR(1) not null,
        date_entered TIMESTAMP not null,
        id Serial primary key
   );
        """
    )

    task2 = PostgresOperator(
        task_id = 'insert_into_table',
        postgres_conn_id = "postgres_localhost",
        sql ="""
            INSERT INTO customer (first_name, last_name, email, company, street, city, state, zip, phone, birth_date, sex, date_entered)
            VALUES ('John', 'Doe', 'johndoe@example.com', 'Acme Inc.', '123 Main St', 'Anytown', 'CA', 12345, '555-555-1212', '1970-01-01', 'M', NOW());

            INSERT INTO customer (first_name, last_name, email, company, street, city, state, zip, phone, birth_date, sex, date_entered)
            VALUES ('Jane', 'Doe', 'janedoe@example.com', 'Acme Inc.', '123 Main St', 'Anytown', 'CA', 12345, '555-555-1212', '1970-01-01', 'F', NOW());
        """
    )
    
    
    # delete duplicates before insert
    task3 = PostgresOperator(
        task_id = 'delete_from_table',
        postgres_conn_id = "postgres_localhost",
        sql ="""
            DELETE FROM customer WHERE first_name = 'John' AND last_name = 'Doe';
            DELETE FROM customer WHERE first_name = 'Jane' AND last_name = 'Doe';
        """
    )
    
    
    # build dependencies
    task1 >> task3 >> task2