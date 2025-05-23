from confluent_kafka import Producer
from dotenv import load_dotenv
import os
import random
import time

load_dotenv()

# Producer configuration
conf = {
    'bootstrap.servers': os.getenv('BOOTSTRAP_SERVERS'),
    'sasl.mechanisms': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    'sasl.username': os.getenv('SASL_USERNAME'),
    'sasl.password': os.getenv('SASL_PASSWORD'),
    'client.id': os.getenv('CLIENT_ID')
}

# Creation of producer
producer = Producer(**conf)

# Callback function to delivery messages
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Producing messages simulating a refrigerator sensor
topic = os.getenv('TOPIC')
for i in range(10):
    temperature = random.uniform(-5, 5)  # Ambient temperature between -5 and 5 degrees Celsius
    key = f"sensor{i % 3}"  # Use different keys to distribute across partitions
    producer.produce(topic, key=key, value=f"{temperature:.2f}", callback=delivery_report)
    producer.poll(0)
    time.sleep(1)  # Simulate temperature reading every second


# Wait until all messages are delivered
producer.flush()