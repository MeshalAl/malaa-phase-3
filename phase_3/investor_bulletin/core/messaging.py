from amqpstorm import Connection, Message
import requests
from malaa_schema.alert_schema import AlertCreate
from tenacity import retry, stop_after_attempt, wait_fixed
from os import environ
from dotenv import load_dotenv
from _config.logger_config import logger

def init_broker():
    load_dotenv()
    hostname = environ.get("RABBITMQ_HOST")
    username = environ.get("RABBITMQ_USER")
    password = environ.get("RABBITMQ_PASSWORD")
    port = int(environ.get("RABBITMQ_PORT"))

    return Connection(hostname=hostname, username=username, password=password, port=port)

@retry(stop=stop_after_attempt(3), wait=wait_fixed(3))
def record_event(message: AlertCreate):

    backend = environ.get('BACKEND_URL')
    alerts_route = environ.get('ALERTS_ROUTE')
    url = f"{backend}/{alerts_route}/"

    headers = {'content-type': 'application/json'}
    payload = message.model_dump_json()

    try:
        response = requests.post(url, data=payload, headers=headers)
        response.raise_for_status()
        logger.info(f"Event recorded: {message.model_dump_json()}")
    except Exception as e:
        logger.warning(f"Attempt failed: {e}")

@retry(stop=stop_after_attempt(3), wait=wait_fixed(3))
def publish_message(broker, message: AlertCreate):

    channel = broker.channel()
    channel.queue.declare("THRESHOLD_ALERTS_QUEUE")
    payload = message.model_dump_json()

    _message = Message.create(channel=channel, body=payload, properties={
        'content_type': 'application/json'
    })
    try:
        _message.publish(routing_key="THRESHOLD_ALERTS_QUEUE")
        logger.info(f"Message published: {message.model_dump_json()}")
    except Exception as e:
        logger.warning(f"Attempt failed: {e}")

    record_event(message)
    channel.close()

if __name__ == "__main__":

    broker = init_broker()
    message = AlertCreate(name="Test Alert", threshold_price=99.13, symbol="AMQP")
    publish_message(broker, message)
