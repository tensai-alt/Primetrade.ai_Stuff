import os
import time
import hmac
import hashlib
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv

load_dotenv()

class BinanceClient:
    BASE_URL = "https://demo-fapi.binance.com"

    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

        if not self.api_key or not self.api_secret:
            raise ValueError("API keys not found")

    def _sign(self, params):
        query_string = urlencode(params, doseq=True)
        return hmac.new(
            self.api_secret.encode(),
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()

    def place_order(self, **params):
        endpoint = "/fapi/v1/order"

        params["timestamp"] = int(time.time() * 1000)

        # REQUIRED for Futures MARKET/LIMIT
        if "type" in params:
            params["type"] = params["type"].replace("_", "")

        params["signature"] = self._sign(params)

        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.post(
            self.BASE_URL + endpoint,
            headers=headers,
            params=params,
            timeout=10
        )

        if response.status_code != 200:
            raise Exception(f"{response.status_code}: {response.text}")

        return response.json()