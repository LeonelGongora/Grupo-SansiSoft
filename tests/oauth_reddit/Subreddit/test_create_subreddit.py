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
from src.assertions.subreddit_assertions import assert_subreddit_creation_failed

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
def test_SCRUM_T41_Crear_un_subreddit_con_nombre_valido(get_token_fixture, get_user_agent):
    """Verifica que un usuario autenticado pueda crear un subreddit con un nombre válido."""
    nombre_subreddit = generar_nombre_unico()
    payload = get_create_subreddit_payload(nombre_subreddit)
    headers = {
        "Authorization": f"bearer {get_token_fixture}",
        "User-Agent": f"{get_user_agent}",
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

