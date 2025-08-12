import requests
import pytest
import os
import uuid
import logging
import jsonschema
from src.payloads.create_subreddit_payload import get_create_subreddit_payload
from src.assertions.subreddit_assertions import (
    assert_subreddit_schema_output
)
from src.assertions.subreddit_assertions import (
    assert_subreddit_created_successfully,
    assert_response_unauthorized,
    assert_response_invalid_name_error,
    assert_response_missing_token,
    assert_response_invalid_subreddit_name,
    assert_response_forbidden,
    assert_subreddit_response_schema
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
@pytest.mark.regression
@pytest.mark.functional
def test_SRQ001_Crear_un_subreddit_con_nombre_valido(get_token_fixture, get_user_agent):
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
    assert_subreddit_created_successfully(response)
    #assert_subreddit_schema_output(response_json)



# SRB-002: Nombre ya existente — Funcional - Negativo
@pytest.mark.smoke
@pytest.mark.regression
def test_SRQ002_crear_subreddit_existente(get_token_fixture, get_user_agent):
    """
    SRB-002: Crear subreddit con nombre ya existente — Funcional - Negativo
    Se espera que la API rechace la creación con un status 400 o 409 y un mensaje indicando que ya existe.
    """
    nombre = "ceniaprueba"  # Asegúrate de que este subreddit ya existe en Reddit
    payload = get_create_subreddit_payload(nombre)
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": f"{get_user_agent}"
    }
    logger.info(f"Intentando crear subreddit ya existente: {nombre}")
    logger.debug(f"Headers: {headers}")
    logger.debug(f"Payload: {payload}")
    response = requests.post(URL, headers=headers, data=payload)
    logger.info(f"Status Code recibido: {response.status_code}")
    logger.debug(f"Response Body: {response.text}")
    response_json = response.json()

    assert_subreddit_created_successfully(response)


 #SRB-003: Token expirado — Funcional - Negativo
@pytest.mark.functional
@pytest.mark.xfail(reason="BUG-001-SR001:Se obtiene un status code de 200 al suscribirse sin tokken ")
def test_SRQ003_token_expirado( get_user_agent):
    nombre = generate_unique_name("SubredditTokenExpirado")
    payload = get_create_subreddit_payload(nombre)
    
    token_invalido = os.getenv("REDDIT_ACCESS_TOKEN_CADUCADO")

    headers = {
        'Authorization': f'bearer {token_invalido}',
        "Content-Type": "application/x-www-form-urlencoded",
         "User-Agent":  f"{get_user_agent}"
    }
    logger.info("Probando creación con token expirado")
    logger.debug(f"Headers: {headers}")
    logger.debug(f"Payload: {payload}")
    response = requests.post(URL, headers=headers, data=payload)
    logger.info(f"Status Code: {response.status_code}")
    logger.debug(f"Response: {response.text}")
    assert_response_unauthorized(response)

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.functional
def test_SRQ004_sin_token( get_user_agent):
    nombre = generate_unique_name("SinToken")
    get_token_fixture = "tokken_invalido"
    payload = get_create_subreddit_payload(nombre)
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent":  f"{get_user_agent}"
    }
    logger.info("Probando creación sin token")
    logger.debug(f"Payload: {payload}")
    logger.debug(f"Headers: {headers}")
    response = requests.post(URL, headers=headers, data=payload)
    logger.info(f"Status Code: {response.status_code}")
    logger.debug(f"Response: {response.text}")

    assert_response_forbidden(response)

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="BUG-002-SR001:Se obtiene un status code de 200 al ingresar solo 3 caracteres en name  ")
def test_SRQ004_nombre_minimo(get_token_fixture,get_user_agent):
    nombre = generate_unique_name("abc")[:3]  # 3 caracteres: debería fallar
    payload = get_create_subreddit_payload(nombre)
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent":  f"{get_user_agent}"
    }
    logger.info("Probando creación con nombre de menos de 3 caracteres")
    logger.debug(f"Payload: {payload}")
    logger.debug(f"Headers: {headers}")

    response = requests.post(URL, headers=headers, data=payload)
    logger.info(f"Status Code: {response.status_code}")
    logger.debug(f"Response: {response.text}")

    assert_response_invalid_name_error(response)


@pytest.mark.functional
@pytest.mark.regression
# SRB-006: Nombre de 21 caracteres — Funcional
@pytest.mark.xfail(reason="BUG-003-SR001:Se obtiene un status code de 200 al ingresar mas de 21 caracteres en el campo name ")
def test_SRQ005_nombre_maximo(get_token_fixture, get_user_agent):
    nombre = generate_unique_name("a" * 15)[:21]
    payload = get_create_subreddit_payload(nombre)
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent":  f"{get_user_agent}"
    }
    logger.info("Probando creación con nombre de 21 caracteres")
    logger.debug(f"Payload: {payload}")
    response = requests.post(URL, headers=headers, data=payload)

    assert_response_invalid_subreddit_name(response)

@pytest.mark.functional
@pytest.mark.regression


# SRB-008: Sin descripción — Funcional
def test_SRQ006_sin_descripcion(get_token_fixture,get_user_agent ):
    nombre = generate_unique_name("SinDescripcion")
    payload = get_create_subreddit_payload(nombre, description="")
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent":  f"{get_user_agent}"
    }
    logger.info("Probando creación sin descripción")
    logger.debug(f"Payload: {payload}")
    response = requests.post(URL, headers=headers, data=payload)

    assert_subreddit_created_successfully(response)


@pytest.mark.regression
@pytest.mark.functional
# SRB-009: Subreddit privado — Funcional
def test_SRQ007_subreddit_privado(get_token_fixture, get_user_agent):
    nombre = generate_unique_name("Privado")
    payload = get_create_subreddit_payload(nombre, subreddit_type="private")
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "Content-Type": "application/x-www-form-urlencoded",
         "User-Agent":  f"{get_user_agent}"
    }
    logger.info("Probando creación de subreddit privado")
    logger.debug(f"Payload: {payload}")
    response = requests.post(URL, headers=headers, data=payload)

    assert_subreddit_created_successfully(response)


@pytest.mark.functional
@pytest.mark.regression
# SRB-010: Subreddit público — Funcional
def test_SRQ009_subreddit_publico(get_token_fixture, get_user_agent):
    nombre = generate_unique_name("Publico")
    payload = get_create_subreddit_payload(nombre, subreddit_type="public")
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent":  f"{get_user_agent}"
    }
    
    logger.info("Probando creación de subreddit público")
    logger.debug(f"Payload: {payload}")
    response = requests.post(URL, headers=headers, data=payload)

    assert_subreddit_created_successfully(response)


# SRB-011: Subreddit con tipo restringido — Funcional
@pytest.mark.functional
@pytest.mark.regression
def test_SRQ010_subreddit_restringido(get_token_fixture, get_user_agent):
    nombre = generate_unique_name("Restringido")
    payload = get_create_subreddit_payload(nombre, subreddit_type="restricted")
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "Content-Type": "application/x-www-form-urlencoded",
       "User-Agent":  f"{get_user_agent}"
    }

    logger.info("Probando creación de subreddit restringido")
    logger.debug(f"Payload: {payload}")
    response = requests.post(URL, headers=headers, data=payload)
    assert_subreddit_created_successfully(response)

# SRB-012: Subreddit con nombre con espacios — Negativo
@pytest.mark.smoke
@pytest.mark.regression
def test_SRQ011_nombre_con_espacios(get_token_fixture, get_user_agent):
    nombre = "Sub reddit"
    payload = get_create_subreddit_payload(nombre)
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent":  f"{get_user_agent}"
    }

    logger.info("Probando creación con espacios en el nombre")
    logger.debug(f"Payload: {payload}")
    response = requests.post(URL, headers=headers, data=payload)

    assert_subreddit_created_successfully(response)
    logger.info("SRB-012: Error correctamente manejado por nombre con espacios")


# SRB-013: Subreddit con nombre en mayúsculas — Funcional
@pytest.mark.functional
@pytest.mark.regression
def test_SRQ012_nombre_mayusculas(get_token_fixture, get_user_agent):
    nombre = generate_unique_name("TESTMAYUS").upper()
    payload = get_create_subreddit_payload(nombre)
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent":  f"{get_user_agent}"
    }

    logger.info("Probando creación con nombre en mayúsculas")
    logger.debug(f"Payload: {payload}")
    response = requests.post(URL, headers=headers, data=payload)

    assert_subreddit_created_successfully(response)
    logger.info(f"SRB-013: Subreddit con nombre en mayúsculas creado exitosamente: {nombre}")

# SRB-014: Subreddit con descripción extensa — Funcional
@pytest.mark.functional
@pytest.mark.regression
def test_SRQ013_descripcion_larga(get_token_fixture, get_user_agent):
    nombre = generate_unique_name("DescLarga")
    descripcion = "Este es un texto de descripción bastante largo. " * 20
    payload = get_create_subreddit_payload(nombre, description=descripcion)
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent":  f"{get_user_agent}"
    }

    logger.info("Probando creación con descripción larga")
    logger.debug(f"Payload: {payload}")
    response = requests.post(URL, headers=headers, data=payload)

    assert_subreddit_created_successfully(response)
    logger.info("SRB-014: Subreddit con descripción extensa creado exitosamente")


# SRB-015: Subreddit con idioma diferente al inglés — Funcional
@pytest.mark.functional
@pytest.mark.regression
def test_SRQ014_idioma_espanol(get_token_fixture, get_user_agent):
    nombre = generate_unique_name("IdiomaES")
    payload = get_create_subreddit_payload(nombre, lang="es")
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent":  f"{get_user_agent}"
    }

    logger.info("Probando creación con idioma español")
    logger.debug(f"Payload: {payload}")
    response = requests.post(URL, headers=headers, data=payload)

    assert_subreddit_created_successfully(response)


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.xfail(reason="BUG-004-SR001:Se obtiene un status code de 200 al ingresar solo espacios en blanco ")
def test_SRQ015_nombre_vacio_con_espacios(get_token_fixture):
    nombre = "     "  # solo espacios
    payload = get_create_subreddit_payload(nombre)
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "MiScriptQA/0.1"
    }

    logger.info("Probando creación con nombre vacío (espacios)")
    logger.debug(f"Payload: {payload}")
    response = requests.post(URL, headers=headers, data=payload)
    assert_response_invalid_subreddit_name(response)
    logger.info("SRB-016: Error correctamente manejado por nombre vacío (espacios)")

