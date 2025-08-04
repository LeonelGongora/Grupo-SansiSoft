from src.services.auth import build_headers
from os import getenv
import os
from dotenv import load_dotenv
import requests

load_dotenv()
def obtener_informacion(username_objetivo):
    payload = {}
    headers = build_headers()
    url = f"{os.getenv('BASE_URL')}user/{username_objetivo}/about"
    response = requests.get(url, headers=headers, data=payload)
    return response

def obtener_informacion_con_token_caducado(username_objetivo):
    payload = {}
    headers = build_headers(token=os.getenv("REDDIT_ACCESS_TOKEN_CADUCADO"))
    url = f"{os.getenv('BASE_URL')}user/{username_objetivo}/about"
    response = requests.get(url, headers=headers, data=payload)
    return response

def obtener_informacion_con_token_invalido(username_objetivo):
    payload = {}
    headers = build_headers(token=os.getenv("REDDIT_TOKEN_INVALIDO"))
    url = f"{os.getenv('BASE_URL')}user/{username_objetivo}/about"
    response = requests.get(url, headers=headers, data=payload)
    return response

def obtener_informacion_con_usuario_vacio():
    payload = {}
    headers = build_headers()
    url = f"{os.getenv('BASE_URL')}user//about"
    response = requests.get(url, headers=headers, data=payload)
    return response