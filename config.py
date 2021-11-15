import os

from dotenv import load_dotenv

load_dotenv() # take environment variables from .env.

API_KEY = os.environ.get('API_KEY')     # Переменные из .env.
API_SECRET = os.environ.get('API_SECRET') # Переменные из .env. 
