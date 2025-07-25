import requests

url = "https://api.restful-api.dev/objects?id=3&id=5&id=10"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)