import requests
from kafka import KafkaProducer
import json
import time

KAFKA_TOPIC = 'coinbase-topic'
KAFKA_BOOTSTRAP_SERVERS = 'localhost:29092'

producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
                         api_version=(0,11,5),
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

def fetch_coinbase_data():
    try:
        response = requests.get("https://criptoya.com/api/argenbtc/btc/ars/0.5")
        if response.status_code == 200:
            response = response.json()
            return response
        else:
            print(f"Failed to fetch data: {response.text}")
            return None
    except Exception as e:
        print(f"Failed to fetch data: {e}")
        return None

def produce_data():
    sent_events = 0
    while sent_events < 5:
        data = fetch_coinbase_data()
        print(f"IS GOING TO SEND: {data}")
        producer.send(KAFKA_TOPIC, value=data)
        print(f"DATA SENT: {data}")
        sent_events += 1
        #time.sleep(20)
    # streaming-1  | Traceback (most recent call last):
    # streaming-1  |   File "/usr/src/app/./streaming.py", line 49, in <module>
    # streaming-1  | ----****THIS IS THE MAIN****----
    # streaming-1  | IS GOING TO SEND: {'ask': 73061729.89, 'totalAsk': 73061729.89, 'bid': 69102720, 'totalBid': 69102720, 'time': 1710166556}
    # streaming-1  |     produce_data()
    # streaming-1  |   File "/usr/src/app/./streaming.py", line 31, in produce_data
    # streaming-1  |     producer.send(KAFKA_TOPIC, value=data)
    # streaming-1  |   File "/usr/local/lib/python3.9/site-packages/kafka/producer/kafka.py", line 576, in send
    # streaming-1  |     self._wait_on_metadata(topic, self.config['max_block_ms'] / 1000.0)
    # streaming-1  |   File "/usr/local/lib/python3.9/site-packages/kafka/producer/kafka.py", line 702, in _wait_on_metadata
    # streaming-1  |     raise Errors.KafkaTimeoutError(
    # streaming-1  | kafka.errors.KafkaTimeoutError: KafkaTimeoutError: Failed to update metadata after 60.0 secs.

if __name__ == "__main__":
    print("----****THIS IS THE MAIN****----")
    produce_data()