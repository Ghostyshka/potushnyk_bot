import os
import requests
from typing import Optional

def get_currency_rate(api_key: str) -> Optional[str]:
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data.get('result') == 'success':
            rates = data['conversion_rates']
            usd_to_uah = rates['UAH']
            return f"1 USD = {usd_to_uah} UAH"
        return None
    except Exception:
        return None