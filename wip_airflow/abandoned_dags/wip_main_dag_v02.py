#general airflow imports
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.mysql_operator import MySqlOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'admin',
    'start_date': datetime(2023, 2, 23),
    'retry':5,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('simple-mysql-dag',
          default_args=default_args,
          schedule_interval='0 0 * * *')

## Spider crawl to s3




## S3 pull task here refferred to as /middleriver.tsv below

toSQL_task = MySqlOperator(dag= dag,
                           mysql_conn_id='mysql_default_conn', 
                           task_id='toSQL_task',
                           sql="LOAD DATA INFILE '/path/to/middleriver.tsv' INTO TABLE middleriver FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n' IGNORE 26 LINES;",
                           )

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

spider_crawl >> s3pull_task >> toSQL_task >> label_pH_task