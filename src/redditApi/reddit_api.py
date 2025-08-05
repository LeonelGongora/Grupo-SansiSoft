from src.services.auth import build_headers
from os import getenv
import os
from dotenv import load_dotenv
from src.payloads.comment_payload import crear_payload_comentario
import requests
from src.logs.logger import logger

load_dotenv()

def comentar_en_post(thing_id, text):
    """Comenta en un post de Reddit."""
    payload = crear_payload_comentario(thing_id, text)
    headers = build_headers()
    url = f"{os.getenv('BASE_URL')}api/comment"

    logger.info("Intentando comentar en un post")
    logger.debug(f"URL: {url}")
    logger.debug(f"Headers: {headers}")
    logger.debug(f"Payload: {payload}")
    response = requests.post(url, headers=headers, data=payload)
    return response


def comentar_en_post_token_erroneo(thing_id, text):
    """Comenta en un post de Reddit con token erróneo."""
    payload = crear_payload_comentario(thing_id, text)
    headers = build_headers(token=None)
    url = f"{getenv('BASE_URL')}api/comment"
    logger.info("Intentando comentar con token erróneo")
    logger.debug(f"URL: {url}")
    logger.debug(f"Headers: {headers}")
    logger.debug(f"Payload: {payload}")

    response = requests.post(url, headers=headers, data=payload)
    return response


def comentar_en_post_token_caducado(thing_id, text):
    """Comenta en un post de Reddit con token caducado."""
    payload = crear_payload_comentario(thing_id, text)
    headers = build_headers(token=os.getenv("REDDIT_ACCESS_TOKEN_CADUCADO"))
    url = f"{getenv('BASE_URL')}api/comment"
    logger.info("Intentando comentar con token caducado")
    logger.debug(f"URL: {url}")
    logger.debug(f"Headers: {headers}")
    logger.debug(f"Payload: {payload}")
    response = requests.post(url, headers=headers, data=payload)
    return response


def obtener_comentarios(thing_id):
    """Obtiene los comentarios de un post de Reddit."""
    headers = build_headers()
    params = {"id": f't1_{thing_id}'}
    url = f"{getenv('BASE_URL')}api/info"
    logger.info("Obteniendo comentarios de un post")
    logger.debug(f"URL: {url}")
    logger.debug(f"Headers: {headers}")
    logger.debug(f"Params: {params}")
    response = requests.get(url, headers=headers, params=params)
    return response


def obtener_comentario_token_sin_token(thing_id):
    """Obtiene un comentario sin token (o token inválido)."""
    headers = build_headers(token=None)
    params = {"id": f't1_{thing_id}'}
    url = f"{getenv('BASE_URL')}api/info"
    logger.info("Intentando obtener comentario sin token")
    logger.debug(f"URL: {url}")
    logger.debug(f"Headers: {headers}")
    logger.debug(f"Params: {params}")
    response = requests.get(url, headers=headers, params=params)
    return response
