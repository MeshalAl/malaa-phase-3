""" Alert Rule Service"""
"""_summary_
this file to write any business logic for the Alert Rules
"""
from resources.alert_rules.alert_rule_schema import AlertRuleCreate
from resources.alert_rules.alert_rule_dal import create_alert_rule, get_alert_rules, update_alert_rule, delete_alert_rule

def create_new_rule_service( rule: AlertRuleCreate, session ):
    return create_alert_rule( rule=rule, session=session)

def get_alert_rules_service(session):
    return get_alert_rules(session)

def update_alert_rule_service(id, rule, session):
    return update_alert_rule(id, rule, session)

def delete_alert_rule_service(id, session):
    return delete_alert_rule(id, session)
