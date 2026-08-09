

1. What is API Authentication?
API authentication verifies that your program is allowed to access a service.
Common methods include:
    Method                          Example
    API Key                     X-API-Key:abc123
    Bearer token                Authorization: Bearer token_here
    Basic authentication         Username and password
    OAuth                       Token-based delegaated access


2. Why Hard-Coding Secrets is Dangerous
Avoid this:
API_KEY = "my-secret-api-key"
Problems:

--The key may be uploaded to GitHub.
--Other people may reuse it.
--The key may be visible in screenshots.
--You may need to edit code whenever the key changes.

Use environment variables instead.

3. Create a .env File
install the packages
    pip install python-dotenv
Create a file named .env:
    API_KEY=your_api_key_here
    API_BASE_URL=https://api.example.com
Do not add quotation marks unless the value really contains them.

7. Add .env to .gitignore
Create or update .gitignore:
    .env
    venv/
    __pycache__/
    *.pyc
The .env file should on your local machine and should not be committed to GitHub
A safe repository usally includes:
    .env .example
Example contents:
    API_KEY=replace_with_your_key
    API_BASE_URL=https://api.example.com
This shows the required variables without exposing real secrets

8. API Key Authentication
Some APIs Expect the key in a header.

headers = {
    "X-API-Key":api_key
}

Some except it is query parameter

params = {
    "api_key": api_key
}

response = requests.get(
    "https://api.example.com/data",
    params=params,
    timeout=10
)

Always folloe the API provider's documentation

9. Bearer Token Authentication
Bearer tokens are usally placed in the Authorization 
header:

headers = {
    "Authorization": f"Bearer {api_key}"
}

header = {
    "Authorization":f"Bearer {api_key}"
}
The word Bearer is part of the standard fromat

