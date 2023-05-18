from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime,timedelta


default_args = {
    "owner": "adamzhang",
    "retries": 5,
    "retry_delay": timedelta(minutes=5)
}


def get_matplotlib_version():
    import matplotlib
    print(f"matplotlib with version {matplotlib.__version__}")
    
def get_sklearn_version():
    import sklearn
    print(f"sklearn with version {sklearn.__version__}")


    
with DAG(
    default_args = default_args,
    dag_id = "dag_with_python_dependencies_v03",
    start_date = datetime(2023,5,18),
    schedule="@daily"
) as dag:
    
    # define a task
    get_matplotlib = PythonOperator(
        task_id = "get_matplotlib",
        python_callable = get_matplotlib_version
    )
    
    get_sklearn = PythonOperator(
        task_id = "get_sklearn",
        python_callable = get_sklearn_version
    )
    
    get_matplotlib >> get_sklearn