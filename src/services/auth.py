import os
import requests
from dotenv import load_dotenv
import logging
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

    res = requests.post(f'https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)
    if res.status_code != 200:
        raise Exception(f"Error autenticando: {res.text}")   
    return res.json()['access_token']



def build_headers(token=None, user_agent=None):
    """
    Construye los headers de autorización y User-Agent de forma dinámica.

    - Si no se proporciona un token, lo toma de la variable de entorno REDDIT_ACCESS_TOKEN.
    - Si no se proporciona un User-Agent, lo toma de la variable de entorno REDDIT_USER_AGENT.
    - Lanza errores si alguno de los valores requeridos no está presente.

    Returns:
        dict: Headers listos para usar en solicitudes HTTP a Reddit.
    """
    token = token or get_token()
    user_agent = user_agent or os.getenv("REDDIT_USER_AGENT")

    if not token:
        raise ValueError("No se proporcionó un token de acceso y no se encontró REDDIT_ACCESS_TOKEN en el entorno.")

    if not user_agent:
        raise ValueError("No se proporcionó un User-Agent y no se encontró REDDIT_USER_AGENT en el entorno.")

    headers = {
        "Authorization": f"Bearer {token}",
        "User-Agent": user_agent
    }
    return headers

def build_headers_sin_authorization(user_agent=None):
    user_agent = user_agent or os.getenv("REDDIT_USER_AGENT")
    headers = {
        "User-Agent": user_agent
    }
    return headers


