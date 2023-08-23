from resources.alert_rules.alert_rule_model import AlertRule
from resources.alerts.alert_model import Alert
from db.database import engine

Alert.metadata.create_all(bind=engine)
AlertRule.metadata.create_all(bind=engine)
