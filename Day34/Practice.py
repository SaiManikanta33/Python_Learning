"""Practice solutions for environment variables, authentication, and status codes."""

import os
from pathlib import Path

import requests
from dotenv import load_dotenv


load_dotenv(Path(__file__).with_name(".env"))


def print_user_details():
    """Exercise 1: load values from .env."""
    print("Username:", os.getenv("USERNAME"))
    print("Role:", os.getenv("ROLE"))


def authenticated_request():
    """Exercise 2: send a request with a deliberately fake Bearer token."""
    headers = {"Authorization": "Bearer fake_token_for_practice"}
    response = requests.get("https://httpbin.org/bearer", headers=headers, timeout=10)
    handle_status_code(response.status_code)
    return response


def require_api_key():
    """Exercise 3: stop clearly when API_KEY has not been configured."""
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise RuntimeError("API_KEY is missing. Add it to your .env file.")
    return api_key


def handle_status_code(status_code):
    """Exercise 5: handle common API responses."""
    if status_code == 200:
        print("200: Request succeeded.")
    elif status_code == 401:
        print("401: Authentication failed. Check the token or API key.")
    elif status_code == 403:
        print("403: Authenticated, but permission is denied.")
    elif status_code == 429:
        print("429: Too many requests. Try again later.")
    elif status_code == 500:
        print("500: The API server had an error.")
    else:
        print(f"Unexpected status code: {status_code}")


if __name__ == "__main__":
    print_user_details()
    require_api_key()

    # Uncomment this after the first two exercises work:
    authenticated_request()

    # Test Exercise 5 without contacting an API:
    for code in (200, 401, 403, 429, 500):
        handle_status_code(code)
