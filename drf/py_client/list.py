import requests
from getpass import getpass

# AUTH
auth_endpoint = "http://localhost:8000/api/auth/"
password = getpass("Enter password: ")

auth_response = requests.post(
    auth_endpoint,
    json={
        'username': 'aradh',
        'password': password
    }
)

print(auth_response.json())

# ACCESS PROTECTED API
if auth_response.status_code == 200:
    token = auth_response.json()['token']

    headers = {
        "Authorization": f"Token {token}"
    }

    endpoint = "http://localhost:8000/api/products/"
    get_response = requests.get(endpoint, headers=headers)

    print(get_response.json())
