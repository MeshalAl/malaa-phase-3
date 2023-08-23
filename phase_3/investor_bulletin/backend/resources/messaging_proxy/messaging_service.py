import os
import requests
from resources.alerts.alert_schema import AlertCreate
from tenacity import retry, stop_after_attempt, wait_fixed
from _config.logger_config import logger

@retry(stop=stop_after_attempt(3), wait=wait_fixed(3))
def publish_message_service(message: AlertCreate):

    messaging_url = os.environ.get('MESSAGING_URL')
    messaging_route = os.environ.get('MESSAGING_ROUTE')

    url = f"{messaging_url}/{messaging_route}/"
    headers = {'content-type': 'application/json'}

    payload = message.model_dump_json()

    try:
        response = requests.post(url, data=payload, headers=headers)
        response.raise_for_status()
        logger.info(f'Messaging via proxy: {message.model_dump_json()}')

    except Exception as e:
        logger.warning(f"Attempt failed: {e}")
