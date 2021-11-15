# coding=utf-8
import ccxt
from config import API_KEY, API_SECRET

#print(ccxt.exchanges)

#for exchange in ccxt.exchanges:
#    print(exchange)
#Подключение к Binance.
exchange = ccxt.binance({
    'apiKey': API_KEY,
    'secret': API_SECRET,
    'enableRateLimit': True,
    'options':{
        'defaultType': 'future',
        },
    })
balance = exchange.fetch_balance() #Запрос баланса Binance.

print(balance['total']['USDT']) #Печать баланса Binance.

#print(exchange)

#markets = exchange.load_markets()

#ticker = exchange.fetch_ticker('BNB/USDT')
#print(ticker)

#for market in markets:
#    print(market)
