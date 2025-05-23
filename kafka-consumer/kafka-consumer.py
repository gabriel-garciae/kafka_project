from confluent_kafka import Consumer, KafkaError
from dotenv import load_dotenv
import os
import csv

load_dotenv()

# Producer configuration
conf = {
    'bootstrap.servers': os.getenv('BOOTSTRAP_SERVERS'),
    'sasl.mechanisms': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    'sasl.username': os.getenv('SASL_USERNAME'),
    'sasl.password': os.getenv('SASL_PASSWORD'),
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(**conf)

# Topic subscription
topic = os.getenv('TOPIC')
consumer.subscribe([topic])

# Function to process messages
def consume_messages():
    # CSV file name
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script directory
    csv_file = os.path.join(script_dir, 'messages.csv')  # Full path to the CSV file
    
    # Open the CSV file in write mode
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Key', 'Value'])  # Write header to the CSV
        
        try:
            while True:
                msg = consumer.poll(1.0)  # Wait up to 1 second for a new message
                # Display the received message
                if msg is None:  # If no message was received
                    continue
                if msg.error():  # If there was an error receiving the message
                    continue
                key = msg.key().decode('utf-8')
                value = msg.value().decode('utf-8')
                print(f"Received message: Key: {key}, Value: {value}")
                # Write the message to the CSV
                writer.writerow([key, value])
        except KeyboardInterrupt:
            pass
        finally:
            print("Closing consumer.")
            consumer.close()

if __name__ == "__main__":
    consume_messages()


