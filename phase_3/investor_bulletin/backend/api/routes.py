from fastapi import FastAPI
from api.controllers.market_controllers import router as MarketRouter
from api.controllers.rules_controllers import router as RulesRouter
from api.controllers.messaging_controllers import router as MessagingRouter
def init_routes(app: FastAPI):
    app.include_router(MarketRouter, prefix="/market-prices", tags=["Market"])
    app.include_router(RulesRouter, prefix="/alerts", tags=["Alerts"])
    app.include_router(MessagingRouter, prefix="/messaging", tags=["Messaging"])
    return app
