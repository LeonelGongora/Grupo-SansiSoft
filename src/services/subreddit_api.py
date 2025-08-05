# src/services/subreddit_api.py
import os
import requests
from dotenv import load_dotenv
from src.services.auth import build_headers  # asegúrate que exista
from payloads.create_subreddit_payload import get_create_subreddit_payload

load_dotenv()

def crear_subreddit(nombre_subreddit, token=None):
    url = f"{os.getenv('BASE_URL')}/api/site_admin"
    payload = get_create_subreddit_payload(nombre_subreddit)
    headers = build_headers(token)

    response = requests.post(url, headers=headers, data=payload)
    return response
