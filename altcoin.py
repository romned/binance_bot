from config import API_KEY, API_SECRET
from binance import Client, client
import pandas as pd
import time

client = Client(API_KEY, API_SECRET)

#if __name__ == "__main__":
x = pd.DataFrame(client.get_ticker())
y = x[x.symbol.str.contains('USDT')]
z = y[~((y.symbol.str.contains('UP')) | (y.symbol.str.contains('DOWN')))]
print(z.sort_values(by='priceChangePercent', ascending=False))

