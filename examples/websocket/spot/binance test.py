from binance.websocket.spot.websocket_client import SpotWebsocketClient as WebsocketClient
from dotenv import load_dotenv

load_dotenv()

def message_handler(message):
    print(message)


ws_client = WebsocketClient()
ws_client.start()

ws_client.mini_ticker(
    symbol='bnbusdt',
    id=1,
    callback=message_handler,
)

# Combine selected streams
ws_client.instant_subscribe(
    stream=['bnbusdt@bookTicker', 'ethusdt@bookTicker'],
    callback=message_handler,
)

# ws_client.stop()
