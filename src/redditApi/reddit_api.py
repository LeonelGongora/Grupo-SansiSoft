# from src.configuration.config import RedditAuthConfig, BASE_URL
from src.services.auth import build_headers
from os import getenv
import os
from dotenv import load_dotenv
from src.payloads.comment_payload import crear_payload_comentario
import requests

load_dotenv()

def comentar_en_post(thing_id, text):
    """ Comenta en un post de Reddit.
        thing_id: ID del post o comentario al que se quiere responder
    """
    payload = crear_payload_comentario(thing_id, text)
    headers = build_headers()
    url = f"{os.getenv('BASE_URL')}api/comment"
    response = requests.post(url, headers=headers, data=payload)
    return response
    

def comentar_en_post_token_erroneo(thing_id, text):
    """ Comenta en un post de Reddit.
        thing_id: ID del post o comentario al que se quiere responder
    """
    payload = crear_payload_comentario(thing_id, text)
    headers = build_headers(token=None)
    url = f"{getenv('BASE_URL')}api/comment"
    response = requests.post(url, headers=headers, data=payload)
    return response
    
def comentar_en_post_token_caducado(thing_id, text):
    """ Comenta en un post de Reddit.
        thing_id: ID del post o comentario al que se quiere responder
    """
    payload = crear_payload_comentario(thing_id, text)
    headers = build_headers(token=os.getenv("REDDIT_ACCESS_TOKEN_CADUCADO"))
    url = f"{getenv('BASE_URL')}api/comment"
    response = requests.post(url, headers=headers, data=payload)
    return response
    