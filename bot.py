from os import access
from config import API_KEY, API_SECRET
from binance import Client
import pandas as pd

#if __name__ == "__main__":
client = Client(API_KEY, API_SECRET)

if __name__ == "__main__":
    print(client.futures_account_balance())
    
