from pydantic import BaseModel

class AlertCreate(BaseModel):
    name: str
    threshold_price: float
    symbol: str
