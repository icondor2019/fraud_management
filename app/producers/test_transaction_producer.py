import json
import uuid
from time import sleep
from kafka import KafkaProducer


class OrderProducer:
    """A simple Kafka producer to send test orders to the 'v1.transactions.check' topic."""
    def __init__(self, bootstrap_servers=['localhost:9092']):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda x: json.dumps(x).encode('utf-8')
        )

    def send_test_order(self, amount: float, payment_type: str):
        order_data = {
            "action": "created",
            "body": {
                "transaction_uuid": str(uuid.uuid4()),
                "client_uuid": str(uuid.uuid4()),
                "amount": amount,
                "payment_type": payment_type}
        }

        print(f"Sending order: {order_data}")
        self.producer.send('v1.transactions.check', value=order_data)
        self.producer.flush()
        return order_data

    def close(self):
        self.producer.close()


if __name__ == "__main__":
    producer = OrderProducer()

    # Send some test orders
    test_orders = [
        (100.0, "credit_card"),
        (1500.0, "wire_transfer")
    ]
    try:
        for amount, payment_type in test_orders:
            producer.send_test_order(amount, payment_type)
            sleep(2)  # Wait 2 seconds between orders
    finally:
        producer.close()
