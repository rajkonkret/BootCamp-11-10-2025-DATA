import os
from dotenv import load_dotenv

load_dotenv() # wczytanie pliku .env jako zmienne środowiskowe
api_key = os.getenv("OPENAI_API_KEY")

print("OPENAI_API_KEY=", api_key)