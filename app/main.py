import json
from kafka import KafkaConsumer
from consumers.kafka_consumer import KafkaConsumerWrapper
from consumers.transaction_consumer import transaction_processor


def kafka_setup():
    topic = 'v1.transactions.check'
    consumer_wrapper = KafkaConsumerWrapper(topic)
    consumer_wrapper.start_consumer(transaction_processor)


if __name__ == "__main__":
    kafka_setup()
