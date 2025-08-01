import requests

def create_post(token, title="Test Post", text="Contenido de prueba"):
    headers = {
        'Authorization': f'bearer {token}',
        'User-Agent': 'SansiSofRFV/0.1 by IceOld4091',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    payload = {
        'api_type': 'json',
        'sr': "u_IceOld4091",
        'kind': 'self',
        'title': title,
        'text': text
    }

    response = requests.post('https://oauth.reddit.com/api/submit', headers=headers, data=payload)

    if response.status_code != 200:
        raise Exception(f"Falló la creación del post: {response.status_code}, {response.text}")

    json_data = response.json()
    return json_data["json"]["data"]["name"]  # ← Esto devuelve el post_id, como "t3_xxxxxx"
