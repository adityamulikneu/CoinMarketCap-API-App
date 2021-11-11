import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5000&convert=USD&CMC_PRO_API_KEY={API_KEY}")

api = json.loads(api_request.content) # Serialization

print(api)

coins = [
    {
        "symbol": "BTC",
        "amount_owned": 2,
        "price_per_coin": 3200
    },
    {
        "symbol": "EOS",
        "amount_owned": 100,
        "price_per_coin": 2.05
    }
]

total_pl = 0

for i in range(0, 500000):
    for coin in coins:
        if api["data"][i]["symbol"] == coin:
            total_paid = coin["amount_owned"] * coin["price_per_coin"]
            current_value = coin["amount_owned"] * api["data"][i]["quote"]["USD"]["price"]
            pl_percoin = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
            total_pl_coin = pl_percoin * coin["amount_owned"]

            total_pl = total_pl + total_pl_coin

            print(api["data"][0]["symbol"])
            print(api["data"][0]["quote"]["USD"]["price"])
            print(total_paid)
            print(current_value)
            print(pl_percoin)
            print("----------------------------------")

print(total_pl)