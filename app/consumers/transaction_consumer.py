import json
import traceback
from loguru import logger
from services.test_fraud_service import FraudService
from producers.decision_producer import TransferDecisionProducer


def transaction_processor(raw_message):
    try:
        message = json.loads(raw_message.value)
        logger.debug(f"Processing transaction: {message}")
        if message['action'] == 'created':
            transaction_data = message['body']
            transaction_uuid = transaction_data['transaction_uuid']

            # Perform fraud assessment
            risk_assessment = FraudService().assess_risk(transaction_data)
            TransferDecisionProducer().send_decision(transaction_uuid=transaction_uuid,
                                                     decision=risk_assessment)
        else:
            logger.debug(f"Ignored message with action: {message['action']}")
    except json.JSONDecodeError as e:
        logger.error(f"Failed to decode message: {str(e)}")
        logger.error(traceback.format_exc())
    except Exception as ex:
        logger.error(f"Error processing message: {str(ex)}")
        logger.error(traceback.format_exc())
