import os
import sys
from datetime import datetime,timedelta
from airflow import DAG
import pandas as pd
from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator


default_args = {
    "owner": "airflow",
    'start_date': datetime(2023, 2, 23),
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


dag = DAG(
    'spider_test2',
    default_args=default_args,
    description='Combine output of two spiders into a single TSV file',
    schedule_interval=None,
)

#ryerisland_spider = '/Users/kenziecarter/Documents/Astro-Airflow/dags/ryerisland_spider.py'
def my_function():
    # Add the directory containing your DAG file to the PYTHONPATH environment variable
    dag_directory = '/Users/kenziecarter/Documents/Astro-Airflow/dags'
    sys.path.insert(0, dag_directory)
    
    # Import your Python script as a module
    import ryerisland_spider
    
    # Call a function in your script
    ryerisland_spider.my_function()

my_task = PythonOperator(
    task_id='my_task',
    python_callable=my_function
)


def ryerisland_spider2():
    import ryerisland_spider.py
    ryerisland_spider.run()

my_task = PythonOperator(
    task_id='my_task',
    python_callable=ryerisland_spider2,
    dag=dag
) 

#t2 = BashOperator(
    #task_id='ryerisland_spider',
    #bash_command='cd {} && scrapy crawl ryerisland_spider'.format(ryerisland_spider),
    #dag=dag)

#t2

my_task