""" Market Schema"""
"""_summary_
This file to abstract any validation logic for the Market
"""


from typing import List
from pydantic import BaseModel, validator

class MarketRequest(BaseModel):
    symbol: str

class MarketResponse(BaseModel):
    price: float

    @validator('price')
    def validate_not_zero(cls, value):
        if value <= 0 or None:
            raise ValueError("Price cannot be 0 or None.")
        return value

class SymbolPricePair(BaseModel):
    symbol: str
    price: float

class MarketPriceResponse(BaseModel):
    price_list: List[SymbolPricePair]
