def validate_order(symbol, side, order_type, quantity, price=None, stop_price=None):
    side = side.upper()
    order_type = order_type.upper()
    symbol = symbol.upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT", "STOP_LIMIT"]:
        raise ValueError("Invalid order type")

    if quantity <= 0:
        raise ValueError("Quantity must be > 0")

    if order_type == "LIMIT" and price is None:
        raise ValueError("LIMIT requires price")

    if order_type == "STOP_LIMIT":
        if price is None or stop_price is None:
            raise ValueError("STOP_LIMIT requires price and stop_price")

    return symbol, side, order_type