from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

from coinbase_fetch import coinbase_fetch
from load_into_minio import load_into_minio

from plugins import send_email

# import sys
# import os
# sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)))
# from airflow.scripts import send_email

#from airflow.scripts.send_email import send_email

# Define default arguments
default_args = {
    'owner': 'data-snacks',
    'start_date': datetime(2023, 9, 29),
    'retries': 1,
}

# Instantiate your DAG
dag = DAG('coinbase_orchestrator', default_args=default_args, schedule_interval=None)

task_1 = PythonOperator(
    task_id='coinbase_fetch',
    python_callable=coinbase_fetch,
    dag=dag,
)

task_2 = PythonOperator(
    task_id='load_into_minio',
    python_callable=load_into_minio,
    dag=dag,
)

# task_3 = PythonOperator(
#     task_id='send_email',
#     python_callable= send_email,
#     dag=dag,
# )


# Set task dependencies
task_1 >> task_2 #>> task_3