from fastapi import APIRouter
from messaging import publish_message, init_broker
from malaa_schema.alert_schema import AlertCreate
router = APIRouter()

@router.post('/')
def publish_message_route(message: AlertCreate):
    broker = init_broker()
    return publish_message(broker=broker, message=message)
