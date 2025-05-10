from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 5, 10),
    'retries': 1,
}

with DAG(
    'docker_python_script_execution',
    default_args=default_args,
    description='Executa um script Python dentro de um container Docker',
    schedule_interval=None,
    catchup=False,
) as dag:

    run_python_script = DockerOperator(
        task_id='run_python_script_in_container',
        image='container-application', 
        command='python /workspace/caminho/do/script.py',
        api_version='auto',
        auto_remove=True,  
        docker_url='unix://var/run/docker.sock',  
        network_mode='bridge', 
    )

    run_python_script 
