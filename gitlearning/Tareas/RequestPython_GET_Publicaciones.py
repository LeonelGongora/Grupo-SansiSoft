import requests

url = "https://jsonplaceholder.typicode.com/posts/23"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
assert response.status_code == 200
print(response.text)
