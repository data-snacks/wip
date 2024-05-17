from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from include.coinbase_fetcher import produce_data
from include.kafka_to_minio import consume_data

start_date = datetime(2018, 12, 21, 12, 12)

default_args = {
    'owner': 'airflow',
    'start_date': start_date,
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

with DAG('crypto_data_stream', 
         default_args=default_args, 
         schedule_interval='*/10 * * * *', 
         catchup=False) as dag:

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

    produce_data >> consume_data