#pip install apache-airflow-providers-amazon

import os
import subprocess
import shutil
from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.mysql_operator import MySqlOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 2, 23),
    'retry':0,
}

with DAG('pull_from_s3_bucket', default_args=default_args, schedule_interval=None) as dag:
    pull_file_task = DockerOperator(
        task_id='pull_file_from_s3',
        image='docker-image-with-s3-python-library',
        api_version='auto',
        auto_remove=True,
        command='/bin/bash -c "python /usr/local/airflow/dags/pull_from_s3.py"',
        volumes=['/path/to/local/dags/folder:/usr/local/airflow/dags'],
        environment={
            'AWS_ACCESS_KEY_ID': 'AWS_ACCESS_KEY_ID',
            'AWS_SECRET_ACCESS_KEY': 'AWS_SECRET_ACCESS_KEY',
        },
    )

pull_file_task