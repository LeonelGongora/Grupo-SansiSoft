import requests
import pytest
import os
from src.logs.logger import logger  
from src.assertions.get_post_assertions import (
    assert_get_post_response_schema,
    assert_status_code,
    assert_required_post_fields_present
)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_OI001_get_post_by_id(get_token_fixture, created_post_id, get_user_agent):
    """Descripción: Consulta un post por ID validando status 200 y la estructura de la respuesta."""

    post_id = created_post_id
    url = f"https://oauth.reddit.com/api/info?id={post_id}"
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        'User-Agent': get_user_agent
    }
    logger.info(f"domain: {url}")
    logger.debug(f"Request headers: {headers}")
    response = requests.get(url, headers=headers)
    response_json = response.json()
    # Validaciones
    logger.info(f"Status code: {response.status_code}")
    logger.debug(f"Respuesta JSON exitoso: {response_json}")
    assert_status_code(response, expected_status=200)
    assert_get_post_response_schema(response_json)

@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.xfail(reason="BUG-LC001: La API responde 200 cuando se debería retornar un error ante ID inexistente")
def test_OI002_get_post_id_nonexistent(get_token_fixture, get_user_agent):
    """
    OI-002: Obtener información de un post con ID inexistente.
    Valida que el status sea 200 y que children esté vacío.
    """
    post_id = "t3_invalidxxx" # ID de post inexistente
    url = f"https://oauth.reddit.com/api/info?id={post_id}"
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        'User-Agent': get_user_agent
    }
    logger.info(f"domain: {url}")
    logger.debug(f"Request headers: {headers}")
    response = requests.get(url, headers=headers)
    response_json = response.json()
    logger.info(f"Status code: {response.status_code}")
    logger.debug(f"Respuesta JSON para ID inexistente: {response_json}")
    # 404 Not Found: El formato del ID es válido (t3_ incluido), pero no existe.
    assert_status_code(response, expected_status=404)
    

@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.xfail(reason="BUG-LC001: La API responde 200 cuando se debería retornar un error ante ID sin prefijo")
def test_OI003_get_post_id_without_prefix(get_token_fixture, get_user_agent):
    """
    OI-003: Obtener información de un post con ID sin prefijo 't3'.
    Valida que el status sea 200 y que children esté vacío.
    """
    post_id = "1mazjyd"  # ID sin prefijo
    url = f"https://oauth.reddit.com/api/info?id={post_id}"
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        'User-Agent': get_user_agent
    }
    logger.info(f"domain: {url}")
    logger.debug(f"Request headers: {headers}")
    response = requests.get(url, headers=headers)
    response_json = response.json()
    logger.info(f"Status code: {response.status_code}")
    logger.debug(f"Respuesta JSON para ID sin prefijo: {response_json}")
    # 400 Bad Request: No cumple el formato requerido por la API, es un error de solicitud.
    assert_status_code(response, expected_status=400)


@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.xfail(reason="BUG-LC001: La API responde 200 cuando se debería retornar un error ante ID sin prefijo")
def test_OI004_get_post_id_invalid_format(get_token_fixture, get_user_agent):
    """
    OI-004: Obtener información de un post con ID con formato inválido.
    Valida que el status sea 200 y que children esté vacío.
    """
    post_id = "%$######"  # Formato inválido
    url = f"https://oauth.reddit.com/api/info?id={post_id}"
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        'User-Agent': get_user_agent
    }
    logger.info(f"domain: {url}")
    logger.debug(f"Request headers: {headers}")
    response = requests.get(url, headers=headers)
    response_json = response.json()
    logger.info(f"Status code: {response.status_code}")
    logger.debug(f"Respuesta JSON para ID con formato inválido: {response_json}")
    # 400 Bad Request: El formato no es válido, se espera un ID alfanumérico bien formado.
    assert_status_code(response, expected_status=400)

@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.xfail(reason="BUG-LC001: La API responde 200 cuando se debería retornar un error ante ID sin prefijo")
def test_OI005_get_post_id_empty(get_token_fixture, get_user_agent):
    """
    OI-005: Obtener información de un post con ID vacío.
    Valida que el status sea 200 y que children esté vacío.
    """
    post_id = ""  # ID vacío
    url = f"https://oauth.reddit.com/api/info?id={post_id}"
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        'User-Agent': get_user_agent
    }
    logger.info(f"domain: {url}")
    logger.debug(f"Request headers: {headers}")
    response = requests.get(url, headers=headers)
    response_json = response.json()
    logger.info(f"Status code: {response.status_code}")
    logger.debug(f"Respuesta JSON para ID vacío: {response_json}")
    # 400 Bad Request: Falta parámetro obligatorio o está vacío.
    assert_status_code(response, expected_status=400)

@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.xfail(reason="BUG-LC001: La API responde 200 cuando se debería retornar un error ante ID sin prefijo")
def test_OI006_get_post_without_query_params(get_token_fixture, get_user_agent):
    """
    OI-006: Obtener información de un post sin incluir query params.
    Valida que el status sea 200 y que children esté vacío.
    """
    url = "https://oauth.reddit.com/api/info"  # Sin parámetros
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        'User-Agent': get_user_agent
    }
    logger.info(f"domain: {url}")
    logger.debug(f"Request headers: {headers}")
    response = requests.get(url, headers=headers)
    response_json = response.json()
    logger.info(f"Status code: {response.status_code}")
    logger.debug(f"Respuesta JSON sin query params: {response_json}")
    # 400 Bad Request: Falta parámetro obligatorio id.
    assert_status_code(response, expected_status=400)

@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.xfail(reason="BUG-LC001: La API responde 200 cuando se debería retornar un error ante ID sin prefijo")
def test_OI008_get_post_id_uppercase(get_token_fixture, created_post_id, get_user_agent):
    """
    OI-008: Verificar si el endpoint es case-sensitive.
    Enviar ID en mayúsculas y validar que retorna 200 y children vacío.
    """
    post_id = created_post_id.lower()
    post_id_upper = post_id.upper()
    url = f"https://oauth.reddit.com/api/info?id={post_id_upper}"
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        'User-Agent': get_user_agent
    }
    logger.info(f"domain: {url}")
    logger.debug(f"Request headers: {headers}")
    response = requests.get(url, headers=headers)
    response_json = response.json()
    logger.info(f"Status code: {response.status_code}")
    logger.debug(f"Respuesta JSON para ID en mayúsculas: {response_json}")
    # 404 Not Found: La API es case-sensitive y no encuentra el recurso.
    assert_status_code(response, expected_status=404)

@pytest.mark.functional
@pytest.mark.regression
def test_OI007_get_post_with_duplicate_query_params(get_token_fixture, created_post_id, get_user_agent):
    """
    OI-007: Obtener información de un post enviando dos veces el mismo query param.
    Valida que el status sea 200 y que children esté vacío.
    """
    post_id = created_post_id
    # URL con dos parámetros 'id'
    url = f"https://oauth.reddit.com/api/info?id={post_id}&id={post_id}"
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        'User-Agent': get_user_agent
    }
    logger.info(f"domain: {url}")
    logger.debug(f"Request headers: {headers}")
    response = requests.get(url, headers=headers)
    response_json = response.json()
    logger.info(f"Status code: {response.status_code}")
    logger.debug(f"Respuesta JSON para ID en mayúsculas: {response_json}")
    # Validar que retorna 200
    assert_status_code(response, expected_status=200)
    assert_get_post_response_schema(response_json)

@pytest.mark.functional
@pytest.mark.regression
def test_OI010_get_post_with_expired_token(get_user_agent, created_post_id):
    """
    OI-010: Intentar obtener un post con token expirado.
    Debería devolver 403 Unauthorized.
    """
    expired_token = os.getenv("REDDIT_ACCESS_TOKEN_CADUCADO")  # Token expirado guardado hace 2 días
    post_id = created_post_id
    url = f"https://oauth.reddit.com/api/info?id={post_id}"
    headers = {
        'Authorization': f'bearer {expired_token}',
        'User-Agent': get_user_agent
    }
    logger.info(f"domain: {url}")
    logger.debug(f"Request headers: {headers}")
    response = requests.get(url, headers=headers)
    logger.info(f"Status code: {response.status_code}")
    logger.debug(f"Respuesta con token expirado: {response.text}")
    assert_status_code(response, expected_status=403)

@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.xfail(reason="BUG-OI-009: status 200 con token vacío")
def test_OI009_get_post_with_empty_token(get_user_agent):
    """
    OI-009: Intentar obtener un post sin token (Authorization vacío).
    Debería devolver 401 Unauthorized.
    """
    empty_token = ""  # Token vacío
    post_id = "t3_exampleid"
    url = f"https://oauth.reddit.com/api/info?id={post_id}"
    headers = {
        'Authorization': f'bearer {empty_token}',
        'User-Agent': get_user_agent
    }
    logger.info(f"domain: {url}")
    logger.debug(f"Request headers: {headers}")
    response = requests.get(url, headers=headers)
    logger.info(f"Status code: {response.status_code}")
    logger.debug(f"Respuesta con token vacío: {response.text}")
    assert_status_code(response, expected_status=401)

@pytest.mark.functional
@pytest.mark.regression
def test_OI011_validate_required_fields_in_post_schema(get_token_fixture, created_post_id, get_user_agent):
    """
    OI-011: Validar que los campos requeridos estén presentes en la respuesta.
    Campos requeridos: subreddit, author_fullname, title, id, url
    """
    post_id = created_post_id
    url = f"https://oauth.reddit.com/api/info?id={post_id}"
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        'User-Agent': get_user_agent
    }
    logger.info(f"domain: {url}")
    logger.debug(f"Request headers: {headers}")
    response = requests.get(url, headers=headers)
    response_json = response.json()
    logger.info(f"Status code: {response.status_code}")
    logger.debug(f"Respuesta JSON para validación de campos requeridos: {response_json}")
    # Validaciones
    assert_status_code(response, expected_status=200)
    assert_required_post_fields_present(response_json)


