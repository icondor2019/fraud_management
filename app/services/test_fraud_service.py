from enum import Enum
from typing import Dict


class Decision(Enum):
    APPROVED = "approved"
    REJECTED = "rejected"
    REVIEW = "review"


class FraudService:
    def __init__(self):
        # Mock thresholds for demonstration
        self.amount_threshold = 1000
        self.high_risk_payment_types = {"crypto", "wire_transfer"}

    def assess_risk(self, transaction_data: Dict) -> Dict:
        """
        Mock risk assessment logic based on amount and payment type
        """
        amount = float(transaction_data.get('amount', 0))
        payment_type = transaction_data.get('payment_type', '')
        order_uuid = transaction_data.get('order_uuid')

        # Mock logic for demonstration
        if amount > self.amount_threshold and payment_type in self.high_risk_payment_types:
            decision = Decision.REJECTED
        elif amount > self.amount_threshold:
            decision = Decision.REVIEW
        else:
            decision = Decision.APPROVED

        return {
            "order_uuid": order_uuid,
            "decision": decision.value
        }
