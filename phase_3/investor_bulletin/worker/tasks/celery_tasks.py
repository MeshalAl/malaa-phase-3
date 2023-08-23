import requests
from app import app
from os import environ
from malaa_schema.alert_schema import AlertCreate
from malaa_schema.alert_rule_schema import AlertRuleCreate
from _config.logger_config import logger

api = environ.get('BACKEND_URL')

def fetch_market_data():
    url = f"{api}/{environ.get('MARKET_PRICES')}"
    market_data = requests.get(url).json().get("price_list")
    if market_data:
        return market_data
    return []

def fetch_alert_rules():
    url = f"{api}/{environ.get('ALERTS_ROUTE')}/{environ.get('ALERT_RULES_ROUTE')}"
    alert_rules = requests.get(url).json()
    if alert_rules:
        return alert_rules
    return []

def find_matching_rules(market_data, alert_rules: list[AlertRuleCreate]):
    matches = []

    for rule in alert_rules:
        for price in market_data:
            if int(price["price"]) < int(rule["threshold_price"]) and price["symbol"] == rule["symbol"]:
                match = {
                    "name": rule["name"],
                    "threshold_price": price["price"],
                    "symbol": price["symbol"]
                }
                matches.append(match)

    return matches

def publish_alerts(matching_alert: AlertCreate, session: requests.Session):

    url = f"{api}/{environ.get('MESSAGING_ROUTE')}/"

    payload = matching_alert.model_dump_json()
    headers = {'content-type': 'application/json'}
    try:
        response = session.post(url, data=payload, headers=headers)
        response.raise_for_status()
        logger.info(f"Message published: {payload}")
    except Exception as e:
        logger.warning(f"Attempt failed: {e}")

@app.task
def publish_alerts_task():

    market_data = fetch_market_data()
    alert_rules = fetch_alert_rules()

    session = requests.Session()

    matches = find_matching_rules(market_data, alert_rules) or []

    if matches:
        for match in matches:
            publish_alerts(AlertCreate(**match), session)
        logger.info(f"Published {len(matches)} alerts")
    else:
        logger.info("No alerts published")

@app.task
def ping():
    logger.info("Pong")
