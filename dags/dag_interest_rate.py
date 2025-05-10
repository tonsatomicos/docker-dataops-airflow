from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime

default_args = {
    'retries': 1,
}

with DAG(
    dag_id='daily_interest_rate_job',
    default_args=default_args,
    start_date=datetime(2025, 5, 10),
    schedule_interval='@daily',
    catchup=False,
    tags=['finance', 'docker'],
) as dag:

    run_script_in_container = DockerOperator(
        task_id='exec_script_in_container',
        image='container-application',
        command='python /workspace/interest-rate-history/core/main.py', 
        auto_remove=True, 
        dag=dag
    )

    run_script_in_container
