from kafka import KafkaProducer
import json
import time
import random

# Configure Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',   # Kafka server address
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize Python dict to JSON string
)

topic_name = 'sales'
sale_id = 1  # Start sale_id counter

print("Starting unlimited message producer. Press Ctrl+C to stop.")

try:
    while True:
        sale_data = {
            'sale_id': sale_id,
            'product': random.choice(['Laptop', 'Phone', 'Tablet', 'Monitor']),
            'quantity': random.randint(1, 5),
            'price': round(random.uniform(100, 1000), 2),
            'timestamp': time.time()
        }
        print(f"Sending: {sale_data}")
        producer.send(topic_name, value=sale_data)
        producer.flush()  # Ensure message is sent immediately
        sale_id += 1
        time.sleep(10)  # Wait 10 seconds before sending the next message
except KeyboardInterrupt:
    print("\nProducer stopped by user.")
finally:
    producer.close()
