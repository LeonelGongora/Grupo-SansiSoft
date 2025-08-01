import os
import requests
from dotenv import load_dotenv

# Cargar variables desde el archivo .env
load_dotenv()

def get_token():
    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    username = os.getenv("REDDIT_USERNAME")
    password = os.getenv("REDDIT_PASSWORD")
    user_agent = os.getenv("REDDIT_USER_AGENT")
    base_url = os.getenv("BASE_URL")
    

    if not all([client_id, client_secret, username, password, user_agent, base_url]):
        raise EnvironmentError("Faltan variables de entorno para la autenticación")

    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)

    data = {
        'grant_type': 'password',
        'username': username,
        'password': password,
        
    }

    headers = {
        'User-Agent': user_agent
    }

    res = requests.post(f'{base_url}api/v1/access_token',
                        auth=auth, data=data, headers=headers)

    if res.status_code != 200:
    
        raise Exception(f"Error autenticando: {res.text}")   
    
    return res.json()['access_token']

def get_headers():
    token = get_token()
    return {
        'Authorization': f'bearer {token}',
        'User-Agent': os.getenv("REDDIT_USER_AGENT"),
        'Content-Type': 'application/x-www-form-urlencoded'
    }
