""" Alert Rule Model """
from db.models.model_base import Base
from sqlalchemy import Column, Integer, String, Float
# use schema to construct the model
class AlertRule(Base):
    __tablename__ = "alert-rules"
    # todo: find why id generated is being rounded up on response. ex: 888632372349173761 -> 888632372349173800 -- swagger rounds up the id.
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    threshold_price = Column(Float)
    symbol = Column(String)
