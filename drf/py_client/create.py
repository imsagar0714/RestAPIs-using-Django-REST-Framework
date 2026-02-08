import requests
endpoint="http://127.0.0.1:8000/api/products/"
data = {
    "title": "mouse",
    "content": "Mechanical keyboard",
    "price": 2500
}
get_response=requests.post(endpoint,json=data)
print(get_response.json())