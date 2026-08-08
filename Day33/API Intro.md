

1. What is an API?
API = Application Programming Interface.
Think of an API as a bridge between two applications.
For Example:
    Your Python Program
        ↓
        API
        ↓
    Weather Service
        ↓
    Weather Data

Your Python program doesn't need to know how the weather service internally works.

IT simple asks:
    "Give me today's weather"
The API returns structured data.

2. What is REST?
REST = Representational State Transfer.

REST API commonly use HTTP methods to interact with resources.

For Example, imagine a /users resource.
    Method              Purpose
    GET                 Retrieve data
    POST                Create
    PUT                 Replace / Update data
    PATCH               Partially update data
    DELETE              Delete data
Example:
    GET/users
means:
    Give me the users


3. HTTP Status Codes
When you make an API request, the server sends a status code.
2xx -- Success
    200     Ok
    201     Created
    204     No Content
4xx -- Client Error
    400     Bad Request
    401     Unauthorized
    403     Forbiddden
    404     Not Found
5xx -- Server Error
    500     Internal Server Error
    502     Bad Gateway
    503     Service Unavailable
A SOC analyst should be comfortable interpreting these codes because they frequently appear in web and application logs.

4. Install requests
Python's requests library makes HTTP requests easy.
install it:
    pip install requests
Check Show requests