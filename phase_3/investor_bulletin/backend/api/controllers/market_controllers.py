from fastapi import APIRouter
from resources.market.market_schema import MarketPriceResponse
from resources.market.market_service import get_market_data

router = APIRouter()

@router.get('/', response_model=MarketPriceResponse)
def get_market_data_route():
    return get_market_data()
