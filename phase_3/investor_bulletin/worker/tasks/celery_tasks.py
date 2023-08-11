import requests
from worker.app import app
from core.messaging import init_broker, publish_message
from os import environ
from resources.alerts.alert_schema import AlertCreate
import logging
'''**Create a celery task that use the market_service.py to fetch the market data and use the rules_service.py to get all the users rules**
'''

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
def publish_alerts_task():
    print('running: publish_alerts_task')

    market_data = fetch_market_data.delay()
    alert_rules = fetch_alert_rules.delay()

    print(market_data, alert_rules)

    broker = init_broker()
    publish_message(broker, AlertCreate(name="Published Alert", threshold_price=100.01, symbol="CELERY"))

@app.task
def ping():
    logger = logging.getLogger(__name__)
    logger.info('pong')
