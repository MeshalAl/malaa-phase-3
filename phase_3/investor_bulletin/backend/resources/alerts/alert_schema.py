""" Alert Schema """
"""_summary_
This file to abstract any validation logic for the Alerts
"""
from pydantic import BaseModel
class AlertCreate(BaseModel):
    name: str
    threshold_price: float
    symbol: str
