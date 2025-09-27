import json
import traceback
from loguru import logger
from app.services.test_fraud_service import FraudService


def transaction_processor(raw_message):
    try:
        header = dict(raw_message.headers)
        logger.debug(f"Message headers: {header}")
        message = json.loads(raw_message.value)
        logger.debug(f"Processing transaction: {message}")
        if message['action'] == 'created':
            transaction_data = message['body']
            fraud_service = FraudService()
            risk_assessment = fraud_service.assess_risk(transaction_data)
            logger.debug(f"Risk assessment result: {risk_assessment}")
        else:
            logger.debug(f"Ignored message with action: {message['action']}")
    except json.JSONDecodeError as e:
        logger.error(f"Failed to decode message: {str(e)}")
        logger.error(traceback.format_exc())
    except Exception as ex:
        logger.error(f"Error processing message: {str(ex)}")
        logger.error(traceback.format_exc())
