import os
from datetime import datetime
import pandas as pd
from airflow.decorators import dag
from astro.files import File
from astro import sql as aql
from astro.sql.table import Metadata, Table
from airflow.operators import BashOperator,PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook

AWS_CONN_ID = "WaterPipelineS3"
SNOWFLAKE_CONN_ID = "snowflake_conn"

with DAG(
    dag_id='spider_test',
    schedule_interval="@daily",
    start_date=datetime(2023, 2, 25),
    catchup=False,
    default_args={
        "retries": 2,  # If a task fails, it will retry 2 times.
    }
    )

# Spiders

ryerisland_spider = BashOperator(
    task_id='ryerisland_spider',
    bash_command='ryerisland_spider.py',
    dag=dag
)

sacramentoriver_spider = BashOperator(
    task_id='ryerisland_spider',
    bash_command='sacramentoriver_spider.py',
    dag=dag
)





ryerisland_spider >> sacramentoriver_spider























#Combine data from Ryer Island and Sacramento River
@aql.transform
def combine_tables(Ryer: Table, Sacr: Table):
    return """
    SELECT *
    FROM {{Ryer}}
    UNION
    SELECT *
    FROM {{Sacr}}
    """

# Switch to Python (Pandas) for melting transformation to get data into long format
@aql.dataframe
def transform_data(df: pd.DataFrame):
    df.columns = df.columns.str.lower()
    melted_df = df.melt(
        id_vars=["sell", "list"], value_vars=["living", "rooms", "beds", "baths", "age"]
    )
    return melted_df

@aql.run_raw_sql
def create_reporting_table():
    """Create the reporting data which will be the target of the append method"""
    return """
    CREATE TABLE IF NOT EXISTS WaterPipelineCombined (
      agency_cd number,
      site_no number,
      datetime varchar,
      tz_cd number,
      XX_0040 number,
      XX_00480 number,
      XX_99133 number,
      XX_0040_cd number,
      XX_00480_cd number,
      XX_99133_cd number
    );
    """