# from src.configuration.config import RedditAuthConfig, BASE_URL
from src.services.auth import get_headers
from os import getenv
from src.payloads.comment_payload import crear_payload_comentario
import requests

def comentar_en_post(thing_id, text):
    """ Comenta en un post de Reddit.
        thing_id: ID del post o comentario al que se quiere responder
    """
    payload = crear_payload_comentario(thing_id, text)
    headers = get_headers()
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    url = f"{getenv('BASE_URL')}api/comment"
    response = requests.post(url, headers=headers, data=payload)
    return response
    