import requests
import time
from kafka import KafkaProducer
from datetime import datetime
import json
#import logging
import os

# COINBASE
COINBASE_API_URL=os.getenv('COINBASE_API_URL','https://api.coinbase.com/v2/prices/spot?currency=USD')

# KAFKA
KAFKA_TOPIC=os.getenv('KAFKA_TOPIC','coinbase-topic')
KAFKA_BOOTSTRAP_SERVERS=os.getenv('KAFKA_BOOTSTRAP_SERVERS','kafka:9092')



def fetch_coinbase_data():
    response = requests.get(COINBASE_API_URL)
    if response.status_code == 200:
        print(f"Success to fetch data: {response.text}") 
        response = response.json()
        return response
    else:
        print(f"Failed to fetch data: {response.text}") 
        #logger.error(f"Failed to fetch data: {response.text}")
        return None

def produce_data():
    producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
                        value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    data = fetch_coinbase_data()
    if data:
        producer.send(KAFKA_TOPIC, data)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print(dt_string)
        #logger.info(f"Data sent to Kafka: {data} at : {dt_string}")
        #time.sleep(10)  # Fetch data every 10 seconds

if __name__ == "__main__":
    produce_data()
