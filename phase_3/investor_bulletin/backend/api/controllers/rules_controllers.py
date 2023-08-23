from fastapi import APIRouter, Depends
from requests import Session
from db.database import get_session
from resources.alerts.alert_service import get_alerts_service, create_new_alert_service
from resources.alert_rules.alert_rule_service import create_new_rule_service,  get_alert_rules_service, update_alert_rule_service, delete_alert_rule_service
from resources.alerts.alert_schema import AlertCreate
from resources.alert_rules.alert_rule_schema import AlertRuleCreate, AlertRuleUpdate, AlertRuleDelete

router = APIRouter()


@router.post('/alert-rules')
def create_alert_rule_route(rule: AlertRuleCreate, session: Session = Depends(get_session)):
    return create_new_rule_service(rule, session)

@router.patch('/alert-rules/{id}')
def update_alert_rule_route(id: int, rule: AlertRuleUpdate, session: Session = Depends(get_session)):
    return update_alert_rule_service(id, rule, session)

@router.delete('/alert-rules/{id}')
def delete_alert_rule_route(id: int, session: Session = Depends(get_session)):
    return delete_alert_rule_service(id, session)

@router.get('/alert-rules')
def get_alert_rules_route(session: Session = Depends(get_session)):
    return get_alert_rules_service(session)

@router.get('/')
def get_alerts_route(session: Session = Depends(get_session)):
    return get_alerts_service(session)

@router.post('/')
def create_new_alert_route(alert: AlertCreate, session: Session = Depends(get_session)):
    return create_new_alert_service(alert, session)
