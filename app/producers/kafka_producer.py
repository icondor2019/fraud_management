import json
from kafka import KafkaProducer
from configuration.settings import settings


class KafkaProducerWrapper:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVER,
            value_serializer=lambda x: json.dumps(x).encode('utf-8')
        )

    def send_message(self, topic: str, msg: dict):
        self.producer.send(topic, value=msg)
        self.producer.flush()

    def close(self):
        self.producer.close()
