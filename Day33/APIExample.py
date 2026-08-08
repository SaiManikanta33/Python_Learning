

    #5.Your First GET Requests
"""
import requests
response = requests.get("https://api.github.com")
print(response.status_code)
print(response.text) 


    #6. Working with JSON
        #Most REST APIs return JSON.
{
    "name":"Mani",
    "role":"Cyber Security Student"
}
    #Python can convert JSON response into python objects. 
    
import requests
response = requests.get("https://api.github.com")
data=response.json()
print(data)
#Can access values like
print(data["current_user_url"])


    #7. Check Whether the Request Was Successful.
import requests
response = requests.get("https://api.github.com")
if response.status_code == 200:
    print("Request successful")
    print(response.json())
else:
    print("Request failed:",response.status_code)
#Even better
    #response.raise_for_status()
"""

import requests
response = requests.post("https://api.github.com")
response.raise_for_status()
print(response.json())
    #If the server returns an HTTP error, raise_for_status() raise an exception
#
#