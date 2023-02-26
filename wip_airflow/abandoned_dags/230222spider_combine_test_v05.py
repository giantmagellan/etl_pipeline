import os
import shutil
import requests
from datetime import datetime, timedelta
import csv

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 2, 24)
}

dag = DAG('scape_combine__output',
          default_args=default_args,
          schedule_interval=None)


def download_dependencies():
    os.system('pip install scrapy')
    os.system('apt-get update && apt-get install -y git')


download_task = BashOperator(
    task_id='download_dependencies',
    bash_command=download_dependencies,
    dag=dag
)


def download_spiders():
    # Create a directory to store the spiders
    os.makedirs('/usr/local/airflow/dags/spiders', exist_ok=True)
    
    # Define the URLs for the spiders
    urls = [
        'https://github.com/giantmagellan/water_use_pipeline/blob/wip_webscraping/waterpipeline/waterpipeline/spiders/middleriver_spider.py',
        'https://github.com/giantmagellan/water_use_pipeline/blob/wip_webscraping/waterpipeline/waterpipeline/spiders/sacramentoriver_spider.py'
    ]
    
    # Download each spider and save it to the spiders directory
    for url in urls:
        response = requests.get(url)
        filename = url.split('/')[-1]
        with open('/usr/local/airflow/dags/spiders/' + filename, 'wb') as f:
            f.write(response.content)

# Define a function to run the spiders and combine the outputs
def run_spiders():
    # Define the command to run the spiders
    command = 'cd /usr/local/airflow/dags && scrapy runspider spiders/spider1.py && scrapy runspider spiders/spider2.py'
    
    # Run the command
    os.system(command)
    
    # Combine the outputs
    outputs = ['/usr/local/airflow/dags/output/spider1_output.tsv', '/usr/local/airflow/dags/output/spider2_output.tsv']
    combined_output = '/usr/local/airflow/dags/output/combined_output.tsv'
    with open(combined_output, 'wb') as outfile:
        for fname in outputs:
            with open(fname, 'rb') as infile:
                shutil.copyfileobj(infile, outfile)

# Define a PythonOperator to download the spiders
download_spiders_operator = PythonOperator(
    task_id='download_spiders',
    python_callable=download_spiders,
    dag=dag,
)

# Define a BashOperator to run the spiders and combine the outputs
run_spiders_operator = BashOperator(
    task_id='run_spiders',
    bash_command='python /usr/local/airflow/dags/run_spiders.py',
    dag=dag,
)

# Define the dependencies between the operators
download_spiders_operator >> run_spiders_operator