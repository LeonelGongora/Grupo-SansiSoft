import requests

url = "https://postman-rest-api-learner.glitch.me//objects?id=ff8081819782e69e019843fad3a9276c"

payload = ""
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
assert response.status_code == 410
