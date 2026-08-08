

    #12. API Authentication
        #Many real APIs require authentication
        #A common pattern is a bearer token
"""
import requests
headers = {
    "Authentication":"Bearer YOUR_API_TOKEN"
}
#Then
response  = requests.get(
    "https://example.com/api/data",
    headers=headers
)
#⚠️ Important Security Rule

#Never hard-code real API keys in your source code.

#❌ Don't do:
API_KEY = "my-secret-key"
#instead , use environment variables:
import os
api_key = os.getenv("API_KEY")
#This connects directly with what you learned on DAY27 about project environments and .env files.
"""
    #13. Error handling
        #Network requests can fail.
import requests
try:
    response = requests.get(
        "https://api.github.com",
        timeout=5
    )
    response.raise_for_status()
    print(response.json())
except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.RequestException as error:
    print("Request failed:",error)
    
#Why timeout?
    #without a timeout, your program could potentially wait too long for a server.