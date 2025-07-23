import requests

url = "https://jsonplaceholder.typicode.com/users/1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    user = response.json()
    print("Nombre:", user['name'])
    print("Email:", user['email'])
    print("Ciudad:", user['address']['city'])
else:
    print("Error al obtener los datos. Código:", response.status_code)
