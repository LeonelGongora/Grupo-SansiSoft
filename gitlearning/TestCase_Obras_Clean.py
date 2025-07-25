import requests

url = "https://api.artic.edu/api/v1/artworks"
params = {
    "fields": "id,title,artist_display,date_display,main_reference_number"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error {response.status_code}: {response.text}")