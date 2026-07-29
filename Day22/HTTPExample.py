"""

import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/2")
print(response.status_code)
print(response.text)

import requests

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10
    )
    print(response.status_code)
    print(response.text)
except requests.RequestException as error:
    print("Request failed:", error)
    
    
    
    
    #3.Working with Json Responses

import requests
url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(url)
data=response.json()
print(data["name"])
print(data["email"])
print(response.text)
print(response.headers)
print(response.status_code)




    #4. Sending Parameters
    
import requests
params={
    "userId":1
}
response = requests.get("https://jsonplaceholder.typicode.com/posts",params=params)
print(response.json())

"""
#5. Sending POST requests

import requests
data = {
    "title":"Python",
    "body":"Learning API's",
    "UserId":1
}
response = requests.post("https://jsonplaceholder.typicode.com/posts",json=data)
print(response.status_code)
print(response.json())



    #6. handling Errors
    
import requests
try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1",timeout=5)
    response.raise_for_status()
    print(response.json())
except requests.exceptions.RequestException as error:
    print("Request failed:",error)