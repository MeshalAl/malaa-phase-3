""" Market Service """
"""_summary_
this file to write any business logic for the Market
"""
import os
import requests
from resources.market.market_schema import MarketRequest, MarketResponse, SymbolPricePair

def get_market_data():

    url = "https://twelve-data1.p.rapidapi.com/price"
    # todo: set keys as env variable.
    headers = {
        "X-RapidAPI-Key": f"{os.environ.get('RAPID_API_KEY')}",
        "X-RapidAPI-Host": f"{os.environ.get('RAPID_API_HOST')}"
    }

    symbols = ['AAPL','MSFT','GOOG','AMZN','META']
    price_data = []
    for symbol in symbols:

        querystring = {"symbol": symbol,"format":"json","outputsize":"30"}

        response = requests.get(url, headers=headers, params=querystring)
        assert response.status_code == 200,  f"Request failed with status code {response.status_code}: {response.text}"

        try:
            request = MarketRequest(symbol=symbol)
            response = MarketResponse(price=response.json().get("price"))
            price_pair = SymbolPricePair(symbol=request.symbol, price=response.price)

            price_data.append(price_pair.model_dump())

        except ValueError as e:
            print(e.json())

    return {'price_list': price_data}
