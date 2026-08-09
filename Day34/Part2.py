

    #6. validate Required Secrets
#A professional program should fail clearly when configuration is missing.
"""
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("d457c02c416a6696825c0d1cca2b8db0")
if not api_key:
    raise RuntimeError("API_KEY is missing. Add it to your .env file.")
#This is safer than silently sending an unauthenticated request


    #10.Handling rate Limits
#APIs may limit number of requests you can make.
#A common response is:
    #429 Too Many Requests
#basic handling:

import time
import requests
response = requests.get(
    "https://api.example.com/data",
    timeout=10
)     
if response.status_code == 429:
    print("Rate limit reached. try again later.")
    time.sleep(5)

#Better approach is to inspect the Retry-After header:
if response.status_code == 429:
    retry_after = response.headers.get("Retry-After", "5")
    print(f"Retry after {retry_after} seconds.")
"""


    #11. Build a Reusable API Client

import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv(Path(__file__).with_name(".env"))


class APIClient:
    def __init__(self):
        self.base_url = os.getenv("API_BASE_URL")
        self.api_key = os.getenv("API_KEY")

        if not self.base_url:
            raise RuntimeError("API_BASE_URL is missing")

        if not self.api_key:
            raise RuntimeError("API_KEY is missing")

    def get_weather(self, city):
        response = requests.get(
            f"{self.base_url}/data/2.5/weather",
            params={
                "q": city,
                "appid": self.api_key,
                "units": "metric",
            },
            timeout=10,
        )

        response.raise_for_status()
        return response.json()


client = APIClient()
data = client.get_weather("Visakhapatnam,IN")
print(data)
print(data["name"])
print(data["main"]["temp"])
print(data["weather"][0]["description"])
#print(headers)      #Unsafe
print("Sending authenticated request")      #Safer

masked_key = f"{self.api_key[:4]}...{self.api_key[-4:]}"
print(masked_key)