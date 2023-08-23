""" Alert Rule  DAL"""
"""_summary_
this file is to right any ORM logic for the Alert Rule model
"""

from resources.alert_rules.alert_rule_schema import AlertRuleCreate, AlertRuleUpdate
from db.models import AlertRule

def create_alert_rule( rule: AlertRuleCreate, session ):
    new_rule = AlertRule(**rule.model_dump())
    session.add(new_rule)
    return {"message": f"Alert Rule created successfully."}

def get_alert_rules(session):
    return session.query(AlertRule).all()

def update_alert_rule(id: int, rule: AlertRuleUpdate, session):

    session.query(AlertRule).filter(AlertRule.id == id).update(rule.model_dump())

    return {"message": f"Alert Rule with id {id} updated successfully."}

def delete_alert_rule(id: int, session):
    session.query(AlertRule).filter(AlertRule.id == id).delete()
    return {"message": f"Alert Rule with id {id} deleted successfully."}
