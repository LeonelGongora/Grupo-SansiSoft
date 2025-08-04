import requests
import pytest
import os
import uuid
import logging
import jsonschema
from src.payloads.create_subreddit_payload import get_create_subreddit_payload
from src.assertions.subreddit_assertions import (
    assert_subreddit_creado_exitosamente,
    assert_subreddit_schema_output
)
from src.assertions.subreddit_assertions import (
    assert_subreddit_created_successfully,
    assert_subreddit_response_schema
)
from src.schemas.subreddit.subreddit_schema_input import input_schema

logger = logging.getLogger(__name__)
BASE_URL = "https://oauth.reddit.com"
ENDPOINT = "/api/site_admin"
URL = BASE_URL + ENDPOINT

def generate_unique_name(base="DEEP_WEB"):
    return f"{base}_{uuid.uuid4().hex[:6]}"

def generar_nombre_unico(base="deepweeb"):
    return f"{base}_{uuid.uuid4().hex[:6]}"


@pytest.mark.smoke
@pytest.mark.functional
def test_SCRUM_T41_Crear_un_subreddit_con_nombre_valido(get_token_fixture):
    """Verifica que un usuario autenticado pueda crear un subreddit con un nombre válido."""
    nombre_subreddit = generar_nombre_unico()
    payload = get_create_subreddit_payload(nombre_subreddit)
    headers = {
        "Authorization": f"bearer {get_token_fixture}",
        "User-Agent": "MiScriptQA/0.1",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    logger.info(f"Host: {BASE_URL}")
    logger.debug(f"POST {URL}")
    logger.debug(f"Headers: {headers}")
    logger.debug(f"Payload: {payload}")

    # Validar contra esquema de entrada
    jsonschema.validate(instance=payload, schema=input_schema)

    response = requests.post(URL, headers=headers, data=payload)
    logger.info(f"Status code: {response.status_code}")
    logger.debug(f"Response body:\n{response.text}")
    assert response.status_code != 403, "403 Forbidden: No tienes permiso para crear subreddits. Verifica tu cuenta/token."
    assert response.status_code in [200, 201], f"Error inesperado: {response.status_code} - {response.text}"
    response_json = response.json()
    # Validaciones
    assert_subreddit_creado_exitosamente(response_json)
    assert_subreddit_schema_output(response_json)
    print(response.text)



# SRB-002: Nombre ya existente — Funcional - Negativo
@pytest.mark.negative
def test_SCRUM_T42_crear_subreddit_existente(get_token_fixture):
    nombre = "ceniaprueba"  # Asegúrate de usar un nombre realmente existente
    payload = get_create_subreddit_payload(nombre)
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "MiScriptQA/0.1"
    }
    response = requests.post(URL, headers=headers, data=payload)

    assert response.status_code in [400, 409], f"Esperado error por nombre duplicado, pero recibí {response.status_code}"
    assert "already exists" in response.text or "SUBREDDIT_EXISTS" in response.text, \
        "No se recibió mensaje de error esperado por subreddit duplicado"

 #SRB-003: Token expirado — Funcional - Negativo
@pytest.mark.negative
def test_SCRUM_T43_token_expirado():
    nombre = generate_unique_name("SubredditTokenExpirado")
    payload = get_create_subreddit_payload(nombre)
    
    token_invalido = os.getenv("TOKEN_CADUCEUS")

    headers = {
        'Authorization': f'bearer {token_invalido}',
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "MiScriptQA/0.1"
    }

    response = requests.post(URL, headers=headers, data=payload)
    
    assert response.status_code == 401, f"Esperado 401 por token expirado, recibido {response.status_code}"
    assert "invalid_token" in response.text or "Unauthorized" in response.text, "No se encontró mensaje de error por token inválido"
    print("✅ SRB-003: El sistema rechazó correctamente el token expirado.")


def test_SCRUM_T44_sin_token():
    nombre = generate_unique_name("SinToken")
    payload = get_create_subreddit_payload(nombre)
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "MiScriptQA/0.1"
    }
    response = requests.post(URL, headers=headers, data=payload)

    assert response.status_code == 401, f"Esperado 401 sin token, recibido {response.status_code}"
    assert "Unauthorized" in response.text, "No se encontró mensaje de autorización requerida"
    print("✅ SRB-004: La API rechazó correctamente la solicitud sin token.")
