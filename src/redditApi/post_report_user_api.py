from src.services.auth import build_headers
from src.services.auth import build_headers_sin_authorization 
from os import getenv
import os
from dotenv import load_dotenv
import requests
from src.payloads.report_user_payload import crear_payload_report_user 
from src.payloads.report_user_payload import crear_payload_report_user_sin_reason 
from src.logs.logger import logger 

load_dotenv()
def reportar_usuario_exitosamente(usuario, razon):
    payload = crear_payload_report_user(usuario, razon)
    headers = build_headers()
    url = f"{os.getenv('BASE_URL')}api/report_user"
    response = requests.post(url, headers=headers, data=payload)
    logger.info(f"IP or domain: {url}")
    logger.debug(f"Request headers: {headers}")
    logger.debug(f"Request payload: {payload}")
    return response

def reportar_usuario_con_token_invalido(usuario, razon):
    payload = crear_payload_report_user(usuario, razon)
    headers = build_headers(token="452fds45")
    url = f"{os.getenv('BASE_URL')}api/report_user"
    response = requests.post(url, headers=headers, data=payload)
    logger.info(f"IP or domain: {url}")
    logger.debug(f"Request headers: {headers}")
    logger.debug(f"Request payload: {payload}")
    return response

def reportar_usuario_sin_token(usuario, razon):
    payload = crear_payload_report_user(usuario, razon)
    headers = build_headers_sin_authorization()
    url = f"{os.getenv('BASE_URL')}api/report_user"
    response = requests.post(url, headers=headers, data=payload)
    logger.info(f"IP or domain: {url}")
    logger.debug(f"Request headers: {headers}")
    logger.debug(f"Request payload: {payload}")
    return response

def reportar_usuario_token_vencido(usuario, razon):
    payload = crear_payload_report_user(usuario, razon)
    headers = build_headers(token=os.getenv("REDDIT_ACCESS_TOKEN_CADUCADO"))
    url = f"{os.getenv('BASE_URL')}api/report_user"
    response = requests.post(url, headers=headers, data=payload)
    logger.info(f"IP or domain: {url}")
    logger.debug(f"Request headers: {headers}")
    logger.debug(f"Request payload: {payload}")
    return response

def reportar_usuario_sin_reason(usuario):
    payload = crear_payload_report_user_sin_reason(usuario)
    headers = build_headers()
    url = f"{os.getenv('BASE_URL')}api/report_user"
    response = requests.post(url, headers=headers, data=payload)
    logger.info(f"IP or domain: {url}")
    logger.debug(f"Request headers: {headers}")
    logger.debug(f"Request payload: {payload}")
    return response