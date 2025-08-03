from src.services.auth import build_headers
from os import getenv
import os
from dotenv import load_dotenv
import requests
from src.payloads.report_user_payload import crear_payload_report_user

load_dotenv()
def reportar_usuario_exitosamente(usuario, razon):
    payload = crear_payload_report_user(usuario, razon)
    headers = build_headers()
    url = f"{os.getenv('BASE_URL')}api/report_user"
    response = requests.post(url, headers=headers, data=payload)
    return response
