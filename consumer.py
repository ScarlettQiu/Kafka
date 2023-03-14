import json
from kafka.consumer import KafkaConsumer

if __name__ == '__main__':
    # Kafka Consumer
    consumer = KafkaConsumer(
        'registered_user',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest'
    )
    for message in consumer:
        print("Registered User = {}".format(json.loads(message.value)))