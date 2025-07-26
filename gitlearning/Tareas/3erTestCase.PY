import requests
import json

url = "https://api.restful-api.dev/objects/ff8081819782e69e019843fad3a9276c"

payload = json.dumps({
  "name": "Fernando MacBook Pro 16",
  "data": {
    "year": 2025,
    "price": 1849.99,
    "CPU model": "Intel Core i9",
    "Hard disk size": "1 TB"
  }
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
assert response.status_code == 404