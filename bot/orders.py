import logging
from bot.retry import retry


class OrderService:
    def __init__(self, client):
        self.client = client

    @retry(max_retries=3)
    def create_order(
        self,
        symbol,
        side,
        order_type,
        quantity,
        price=None,
        stop_price=None
    ):
        try:
            # Base params
            params = {
                "symbol": symbol,
                "side": side,
                "quantity": quantity,
            }

            # MARKET
            if order_type == "MARKET":
                params["type"] = "MARKET"

            # LIMIT
            elif order_type == "LIMIT":
                params.update({
                    "type": "LIMIT",
                    "price": price,
                    "timeInForce": "GTC"
                })

            # STOP-LIMIT (Binance uses STOP)
            elif order_type == "STOP_LIMIT":
                params.update({
                    "type": "STOP",
                    "price": price,
                    "stopPrice": stop_price,
                    "timeInForce": "GTC"
                })

            else:
                raise ValueError(f"Unsupported order type: {order_type}")

            logging.info(f"[REQUEST] {params}")

            response = self.client.place_order(**params)

            logging.info(f"[RESPONSE] {response}")

            return response

        except Exception as e:
            logging.error(f"[ERROR] {str(e)}")
            raise