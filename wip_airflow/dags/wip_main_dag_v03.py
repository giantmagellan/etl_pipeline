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

subprocess.run(['apt-get', 'update'])
subprocess.run(['apt-get', 'install', '-y', 'git'])

dag = DAG(
    'combine_spider_output',
    default_args=default_args,
    description='Combine output of two spiders into a single TSV file',
    schedule_interval=None,
)

def scrape_spider(git_url, spider_name):
    # Clone the repository
    repo_dir = '/tmp/repo'
    subprocess.run(['git', 'clone', git_url, repo_dir])
    
    # Run the spider
    subprocess.run(['scrapy', 'crawl', spider_name, '-o', f'{spider_name}.tsv'])
    
    # Remove the cloned repository
    shutil.rmtree(repo_dir)

def combine_output():
    # Combine the output of both spiders
    output_dir = '/usr/local/airflow/dags/output'
    output_file = f'{output_dir}/combined_output_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.tsv'
    with open(output_file, 'wb') as wfd:
        for i, tsv_file in enumerate(os.listdir(output_dir)):
            with open(f'{output_dir}/{tsv_file}', 'rb') as fd:
                if i != 0:
                    fd.readline()
                shutil.copyfileobj(fd, wfd)
                    
    # Remove the individual TSV files
    for tsv_file in os.listdir(output_dir):
        os.remove(f'{output_dir}/{tsv_file}')

# Define the tasks
middleriver = PythonOperator(
    task_id='scrape_spider1',
    python_callable=scrape_spider,
    op_kwargs={'git_url': 'https://github.com/giantmagellan/water_use_pipeline/blob/wip_webscraping/waterpipeline/waterpipeline/spiders/middleriver_spider.py',
                'spider_name': 'middleriver'},
    dag=dag,
)

sacramentoriver = PythonOperator(
    task_id='scrape_spider2',
    python_callable=scrape_spider,
    op_kwargs={'git_url': 'https://github.com/giantmagellan/water_use_pipeline/blob/wip_webscraping/waterpipeline/waterpipeline/spiders/sacramentoriver_spider.py',
                'spider_name': 'sacramentoriver'},
    dag=dag,
)

# EDIT THIS FROM NEW GIT PULL
# toSQL_task = MySqlOperator(dag= dag, 
# #mysql_conn_id='mysql_default_conn', 
# #task_id='toSQL_task',
# #sql="LOAD DATA INFILE '/path/to/middleriver.tsv' INTO TABLE middleriver FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n' IGNORE 26 LINES;",
#dag=dag
#)

label_pH_task = MySqlOperator(
    task_id='label_pH',
    mysql_conn_id='mysql_default_conn',
    sql="""
        SELECT
          pH_value,
          CASE 
            WHEN pH_value >= 7.5 THEN 'high'
            WHEN pH_value >= 6.5 AND pH_value < 7.5 THEN 'medium'
            ELSE 'low'
          END AS pH_label
        FROM
          middleriver;
    """,
    dag=dag
)

# Define the task dependencies
middleriver >> sacramentoriver

#middleriver >> toSQL_task
#sacramentoriver >> toSQL_task
#oSQL_task >> label_pH_task
