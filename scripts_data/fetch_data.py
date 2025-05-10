import requests
import pandas as pd
from datetime import datetime

def fetch_top_coins(limit=10):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": limit,
        "page": 1,
        "sparkline": False
    }
    response = requests.get(url, params=params)
    data = response.json()
    df = pd.DataFrame(data)
    df['timestamp'] = datetime.utcnow()
    return df

if __name__ == "__main__":
    df = fetch_top_coins()
    df.to_csv("data/top_coins.csv", index=False)
    print("✅ Data saved to data/top_coins.csv")
