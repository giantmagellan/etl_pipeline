#Imports
import os
import sys
from datetime import datetime,timedelta
from airflow import DAG
import pandas as pd
import subprocess
from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
from include.sacramentoriver_spider import WaterSpider

#Definitions


#Default Arguments Chunk
default_args = {
    "owner": "airflow",
    'start_date': datetime(2023, 2, 23),
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
}


#DAG Tasks
with DAG('spider_test4',
    default_args=default_args,
    description='Combine output of two spiders into a single TSV file',
    schedule_interval=None) as dag:
    
    sacramento_spider_task = PythonOperator(task_id='sacramento_spider_task',
                                       python_callable=WaterSpider().start_requests)

#Ordering
sacramento_spider_task