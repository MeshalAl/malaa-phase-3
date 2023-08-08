""" Alert Model """

"""- [ ] **Setup your ORM models (RuleAlerts, Alerts) and connect them with the DB server**
alerts should have the following properties `name, threshold price, symbol`"""

from db.models.model_base import Base
from sqlalchemy import Column, Integer, String, Float
class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    threshold_price = Column(Float)
    symbol = Column(String)
