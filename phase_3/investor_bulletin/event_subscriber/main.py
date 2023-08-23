from pika import BlockingConnection, ConnectionParameters
from os import environ
from _config.logger_config import logger

# Create a connection object to start consuming events

def init_subscriber():
  broker = environ.get("BROKER")
  broker_port = environ.get("BROKER_PORT")

  connection =  BlockingConnection(ConnectionParameters(host=broker, port=broker_port))
  channel = connection.channel()
  channel.queue_declare(queue="THRESHOLD_ALERTS_QUEUE")
  return channel

def on_event(ch, method, properties, body):
  logger.info(f"Alert received: {body}")

if __name__ == "__main__":

    subscriber = init_subscriber()
    subscriber.basic_consume(queue="THRESHOLD_ALERTS_QUEUE", on_message_callback=on_event)
    subscriber.start_consuming()
    subscriber.close()
