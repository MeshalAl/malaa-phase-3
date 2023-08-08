from db.database import get_session
from resources.market.market_service import get_market_data
from resources.alert_rules.alert_rule_service import get_alert_rules_service
from worker.app import app
from core.messaging import init_broker, publish_message

from resources.alerts.alert_schema import AlertCreate

'''**Create a celery task that use the market_service.py to fetch the market data and use the rules_service.py to get all the users rules**
'''

@app.task
def fetch_market_and_rules_data():
    from db.database import get_session

    session = next(get_session())
    fetched_alert_rules =  get_alert_rules_service(session)
    session.close()
    return fetched_alert_rules, get_market_data()

@app.task
def publish_alerts_task():
    alert_rules, market_data = fetch_market_and_rules_data.delay()
    broker = init_broker()
    publish_message(broker, AlertCreate(name="Published Alert", threshold_price=99.13, symbol="AMQP"))
