import typer
from rich import print

from bot.client import BinanceClient
from bot.orders import OrderService
from bot.validators import validate_order
from bot.logging_config import setup_logger

app = typer.Typer()


@app.command()
def trade(
    symbol: str = typer.Option(...),
    side: str = typer.Option(...),
    order_type: str = typer.Option(...),
    quantity: float = typer.Option(...),
    price: float = typer.Option(None),
    stop_price: float = typer.Option(None),
):
    """
    Place order on Binance Futures Testnet
    """

    setup_logger()

    try:
        symbol, side, order_type = validate_order(
            symbol, side, order_type, quantity, price, stop_price
        )

        print("\n[bold cyan]Order Summary[/bold cyan]")
        print(f"Symbol      : {symbol}")
        print(f"Side        : {side}")
        print(f"Type        : {order_type}")
        print(f"Quantity    : {quantity}")
        print(f"Price       : {price}")
        print(f"Stop Price  : {stop_price}")

        confirm = typer.confirm("Proceed?")
        if not confirm:
            print("[red]Cancelled[/red]")
            raise typer.Exit()

        client = BinanceClient()
        service = OrderService(client)

        response = service.create_order(
            symbol,
            side,
            order_type,
            quantity,
            price,
            stop_price
        )

        print("\n[green]Order Successful[/green]")
        print(f"Order ID     : {response.get('orderId')}")
        print(f"Status       : {response.get('status')}")
        print(f"Executed Qty : {response.get('executedQty')}")
        print(f"Avg Price    : {response.get('avgPrice', 'N/A')}")

    except Exception as e:
        print(f"[red]Error: {str(e)}[/red]")


if __name__ == "__main__":
    app()