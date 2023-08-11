import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
sys.path.append(root_dir)
from amqpstorm import Connection, Message
from resources.alerts.alert_schema import AlertCreate
# Create a connection object to publish events

def init_broker():
    return Connection(hostname="localhost", username="guest", password="guest", port=5672)

def record_event(message: AlertCreate):
    from resources.alerts.alert_service import create_new_alert_service
    from db.database import get_session

    session = next(get_session())
    create_new_alert_service(message, session)
    session.close()

def publish_message(broker, message: AlertCreate):
    channel = broker.channel()
    channel.queue.declare("THRESHOLD_ALERTS_QUEUE")

    payload = message.model_dump_json()
    _message = Message.create(channel=channel, body=payload, properties={
        'content_type': 'application/json'
    })

    _message.publish(routing_key="THRESHOLD_ALERTS_QUEUE")
    channel.close()
    record_event(message)

if __name__ == "__main__":

    broker = init_broker()
    message = AlertCreate(name="Published Alert", threshold_price=99.13, symbol="AMQP")

    publish_message(broker, message)
