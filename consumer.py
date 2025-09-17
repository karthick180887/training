from kafka import KafkaConsumer
import json

# Kafka configuration
bootstrap_servers = 'localhost:9092'
topic_name = 'sales'
output_file = 'sales_messages.jsonl'  # File to save messages

# Create Kafka consumer
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset='earliest',  # Read from the beginning if no offset is stored
    enable_auto_commit=True,
    group_id='sales-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))  # Deserialize JSON messages
)

print(f"Consuming messages from topic '{topic_name}' and saving to '{output_file}'")

# Open file to save messages
with open(output_file, 'a') as file:
    for message in consumer:
        data = message.value
        print(f"Received: {data}")
        file.write(json.dumps(data) + "\n")
        file.flush()  # Ensure it's written to disk
