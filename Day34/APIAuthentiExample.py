

    #A typical authenticated requests looks like this.
"""
import requests

headers = {
    "Authorization": "Bearer your_real_token"
}

response = requests.get(
    "https://real-api-domain.com/data",
    headers=headers,
    timeout=10
)

print(response.status_code)
"""


    #4. Read Environment variables in python
import os
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("d457c02c416a6696825c0d1cca2b8db0")
base_url=os.getenv("https://api.openweathermap.org")
print("API Key loaded:",bool(api_key))
print("Base URL:",base_url)


    #5.Send an Authenticated Request
import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("d457c02c416a6696825c0d1cca2b8db0")
base_url = os.getenv("https://api.openweathermap.org")

    
try:
    response = requests.get(
        f"{base_url}/data/2.5/weather",
        params={
            "q": "Hyderabad,IN",
            "appid": api_key,
            "units": "metric",
        },
        timeout=10,
    )

    response.raise_for_status()
    print(response.json())

except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)

except requests.exceptions.RequestException as error:
    print("Request failed:", error)

