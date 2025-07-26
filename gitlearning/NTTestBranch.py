import requests

url = "https://api.artic.edu/api/v1/artworks?fields=id,title,artist_display,date_display,main_reference_number"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
