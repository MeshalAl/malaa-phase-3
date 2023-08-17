import requests
from worker.app import app
from core.messaging import init_broker, publish_message
from os import environ
from resources.alerts.alert_schema import AlertCreate


api = environ.get('API_URL')

@app.task
def fetch_market_data():
    url = f"{api}/{environ.get('MARKET_PRICES')}"
    market_data = requests.get(url).json()
    if market_data:
        return market_data
    return None

@app.task
def fetch_alert_rules():
    url = f"{api}/{environ.get('ALERT')}/{environ.get('ALERT_RULES')}"
    alert_rules = requests.get(url).json()
    if alert_rules:
        return alert_rules
    return None

@app.task
def find_matching_rules(market_data, alert_rules):
    return [
        {"name": rule["name"], "threshold_price": price["price"], "symbol": price["symbol"]}
        for rule in alert_rules
        for price in market_data
        if price["price"] < rule["threshold_price"] and price["symbol"] == rule["symbol"]
    ]

@app.task
def publish_alerts_task():
    print('running: publish_alerts_task')

    market_data = fetch_market_data.run().get()
    alert_rules = fetch_alert_rules.run().get()

    print(market_data, alert_rules)

    broker = init_broker()

    for match in find_matching_rules.run(market_data, alert_rules).get():
        publish_message(broker, AlertCreate(**match))
    publish_message(broker, AlertCreate(name="Published Alert", threshold_price=100.01, symbol="CELERY-LAST"))

@app.task
def ping():
    return 'pong'
