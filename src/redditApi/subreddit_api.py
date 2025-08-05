import os
import requests
from dotenv import load_dotenv
from src.payloads.create_subreddit_payload import get_create_subreddit_payload
from src.services.auth import build_headers  # Debes tener ya este método
load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://oauth.reddit.com")
ENDPOINT = "/api/site_admin"

def crear_subreddit(nombre_subreddit):
    payload = get_create_subreddit_payload(nombre_subreddit)
    headers = build_headers()
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    url = BASE_URL + ENDPOINT
    response = requests.post(url, headers=headers, data=payload)
    return response
