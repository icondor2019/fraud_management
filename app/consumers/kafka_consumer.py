from kafka import KafkaConsumer
from loguru import logger
import traceback


class KafkaConsumerWrapper:
    def __init__(self, topic):
        self.topic = topic
        self.group_id = 'fraud_risk_group'
        self.bootstrap_servers =['localhost:9092']
        self.consumer = None

    def start_consumer(self, message_processor):
        try:
            self.consumer = KafkaConsumer(
                bootstrap_servers=self.bootstrap_servers,
                auto_offset_reset='earliest',
                enable_auto_commit=True,
                group_id=self.group_id,
                value_deserializer=lambda x: x.decode('utf-8')
            )
            self.consumer.subscribe([self.topic])
            logger.info(f"Kafka consumer started for topic: {self.topic}")
        except Exception as ex:
            logger.error(f"Failed to start Kafka consumer: {str(ex)}")
            traceback.print_exc()

        # Start consuming messages
        self.consume_messages(message_processor)

    def consume_messages(self, message_procesor):
        if not self.consumer:
            logger.error("Consumer not started. Call start() before consuming messages.")
            return
        try:
            for message in self.consumer:
                logger.info(f"Received message: {message.value}")
                message_procesor(message)
                self.consumer.commit()
        except Exception as e:
            logger.error(f"Error while consuming messages: {str(e)}")
            traceback.print_exc()
        finally:
            self.close()

    def close_consumer(self):
        if self.consumer:
            self.consumer.close()
            logger.info("Kafka consumer closed.")
