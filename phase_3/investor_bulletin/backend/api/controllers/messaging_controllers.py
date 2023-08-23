from fastapi import APIRouter
from resources.messaging_proxy.messaging_service import publish_message_service
from resources.alerts.alert_schema import AlertCreate
router = APIRouter()

@router.post('/')
def publish_message_route(message: AlertCreate):
    return publish_message_service(message)
