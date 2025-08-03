import requests
import os
from dotenv import load_dotenv
from src.payloads.payload_crear_post import get_create_post_payload

load_dotenv()

def create_post(token, title="Test Post", text="Contenido de prueba", user_agent=""):
    headers = {
        'Authorization': f'bearer {token}',
        'User-Agent': user_agent,
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    payload = get_create_post_payload(
        subreddit=f"u_{os.getenv('REDDIT_USERNAME')}",
        title=title,
        text=text,
    )

    response = requests.post('https://oauth.reddit.com/api/submit', headers=headers, data=payload)

    if response.status_code != 200:
        raise Exception(f"Falló la creación del post: {response.status_code}, {response.text}")

    json_data = response.json()
    return json_data["json"]["data"]["name"] 
