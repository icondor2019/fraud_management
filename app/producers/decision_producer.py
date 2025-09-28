from loguru import logger
from producers.kafka_producer import KafkaProducerWrapper


class TransferDecisionProducer:
    def __init__(self):
        self.producer = KafkaProducerWrapper()
        self.kafka_topic = "v1.transfer.fraud_decision"

    def send_decision(self, transaction_uuid: str, decision: str):
        decision_data = {
            "transaction_uuid": transaction_uuid,
            "decision": decision
        }
        try:
            self.producer.send_message(
                topic=self.kafka_topic,
                msg=decision_data)
            logger.debug(f"Sent decision: {decision_data} to topic: {self.kafka_topic}")
        finally:
            self.producer.close()
