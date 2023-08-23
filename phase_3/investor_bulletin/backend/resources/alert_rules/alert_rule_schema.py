""" Alert Rule Schema """
"""_summary_
This file to abstract any validation logic for the Alert Rules
"""
from pydantic import BaseModel

class AlertRuleCreate(BaseModel):
    name: str
    threshold_price: float
    symbol: str
class AlertRuleUpdate(BaseModel):
    name: str
    threshold_price: float
    symbol: str
class AlertRuleDelete(BaseModel):
    id: int
