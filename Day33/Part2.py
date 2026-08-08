
    #8. Query Parameters
#Suppose an API accepts:
    #?page=1
        #You can pass parameters using params
"""

import requests
params={
    "page":1
}
response = requests.Request(
    "GET",
    "https://example.com/api/users",
    params=params
).prepare()
print(response.url)
#You don't need to manually construct the URL
    
    #9. Headers
        #HTTP headers provide addtional information about a request

import requests
headers={
    "USer-Agent":"Python-Security-Tool"
}
response = requests.get(
    "https://api.github.com",
    headers=headers
)
print(response.status_code)


    Headers are commonly used for:
    . Authentication
    . Content type
    . User-Agent
    . API Keys
    . Authorization tokens

    #10. POST Request
        #GET retrieves data
        #POST usally sends data to the server to create something
import requests
data={
    "name":"Mani",
    "role":"Cyber Security"
}
response = requests.post(
    "https://httpbin.org/post",
    json = data
)
print(response.status_code)
print(response.json())
"""


    #11. PUT and DELETE
        # PUT
import requests
response = requests.put(
    "https://example.com/api/users/1",
    json={"name":"Mani"}
    )
print(response)

    #DELETE
import requests
response = requests.delete(
    "https://example.com/api/users/1"
)
print(response.status_code)
    #Only use these against APIs where you have permission to modify data.
#