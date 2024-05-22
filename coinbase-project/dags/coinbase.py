from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from include.coinbase_fetcher import produce_data
from include.kafka_to_minio import consume_data

start_date = datetime(2024, 5, 21, 12, 00)

default_args = {
    'owner': 'airflow',
    'start_date': start_date,
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

with DAG('crypto_data_stream', 
         default_args=default_args, 
         schedule_interval=None, 
         catchup=False) as dag:

    start_task = DummyOperator(
        task_id='start',
        dag=dag,
    )

    produce_data_task = PythonOperator(
        task_id='produce_data',
        python_callable=produce_data,
        dag=dag,
    )

    consume_data_task = PythonOperator(
        task_id='consume_data',
        python_callable=consume_data,
        dag=dag,
    )

    end_task = DummyOperator(
        task_id='end',
        dag=dag,
    )

    start_task >> produce_data_task >> consume_data_task >> end_task
