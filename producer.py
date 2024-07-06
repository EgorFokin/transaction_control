from confluent_kafka import Producer
import time

conf = {'bootstrap.servers': 'kafka:9092'}

producer = Producer(conf)

i = 0

while True:
    message = f"message {i}"
    producer.produce('transactions', value=message)
    print(f"Produced: {message}")
    time.sleep(1)
    i += 1

producer.flush()
