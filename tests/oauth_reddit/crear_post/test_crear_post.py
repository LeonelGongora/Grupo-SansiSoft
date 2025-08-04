import requests
import pytest
import os
from dotenv import load_dotenv
from src.logs.logger import logger 
load_dotenv()
from src.assertions.post_assertions import (
    assert_post_response_schema, 
    assert_post_created_successfully, 
    assert_payload_matches_schema,
    assert_response_has_errors
)
from src.payloads.payload_crear_post import get_create_post_payload
from src.redditApi.headers_post import get_create_post_headers
from src.assertions.get_post_assertions import assert_status_code

@pytest.mark.smoke
@pytest.mark.functional

@pytest.mark.ejecutar
def test_CP001_create_post(get_token_fixture):
    """Descripción: Crea un post exitoso validando status 200 y estructura del payload y respuesta."""
    url = "https://oauth.reddit.com"
    headers = get_create_post_headers(
        token=get_token_fixture,
        user_agent=get_user_agent,
        content_type="application/x-www-form-urlencoded"
    )
    payload = get_create_post_payload(
        subreddit=f"u_{os.getenv('REDDIT_USERNAME')}",
        title='Buenas, que opinan de este post?',
        text='No leo los comentarios, pero me gusta verlos',
    )

      # Validación del payload antes de enviar 
    assert_payload_matches_schema(payload)

    submit_url = f"{url}/api/submit"

    response = requests.post(submit_url, headers=headers, data=payload)
    response_json = response.json()
    logger.debug(f"Respuesta JSON al crear post exitoso: {response_json}")
    # Assertions
    assert_post_created_successfully(response)
    print(response_json["json"]["data"]["url"])
    assert_post_response_schema(response_json)

@pytest.mark.functional
@pytest.mark.regression
def test_CP003_create_post_en_subreddit_inexistente(get_token_fixture, get_user_agent):
    """
    CP-003: Crear post en un subreddit inexistente.
    Se espera que si el subreddit no existe, la API retorne un error con status 200.
    """
    url = "https://oauth.reddit.com"
    headers = get_create_post_headers(
        token=get_token_fixture,
        user_agent=get_user_agent,
        content_type="application/x-www-form-urlencoded"
    )
    payload = get_create_post_payload(
        subreddit='subreddit_inexistente_123456',
        title='Intentando postear en un subreddit inexistente',
        text='Este contenido no debería ser aceptado',
    )

    assert_payload_matches_schema(payload)

    response = requests.post(f"{url}/api/submit", headers=headers, data=payload)
    response_json = response.json()
    logger.debug(f"Respuesta JSON al intentar postear en subreddit inexistente: {response_json}")
    # Validaciones esperadas para error
    assert_status_code(response, expected_status=200)
    assert_response_has_errors(response_json)

@pytest.mark.functional
@pytest.mark.regression
def test_CP004_create_post_sin_titulo(get_token_fixture, get_user_agent):
    """
    CP-004: Crear post sin título.
    Se espera que la API retorne un error indicando que el título es obligatorio.
    """
    url = "https://oauth.reddit.com"
    headers = get_create_post_headers(
        token=get_token_fixture,
        user_agent=get_user_agent,
        content_type="application/x-www-form-urlencoded"
    )
    payload = get_create_post_payload(
        subreddit=f"u_{os.getenv('REDDIT_USERNAME')}",
        title="",                        # Título vacío
        text="Contenido sin título"
    )

    response = requests.post(f"{url}/api/submit", headers=headers, data=payload)
    response_json = response.json()
    logger.debug(f"Respuesta JSON al postear sin título: {response_json}")

    assert_status_code(response, expected_status=200)
    assert_response_has_errors(response_json)

@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.xfail(reason="BUG-CP008: El servidor acepta un payload sin 'api_type' y no reporta errores en la respuesta JSON")
def test_CP008_create_post_sin_api_type(get_token_fixture, get_user_agent):
    """
    CP-008: Crear post sin el campo 'api_type'.
    Se espera que la API retorne un error ya que 'api_type' es obligatorio.
    """
    url = "https://oauth.reddit.com"
    headers = get_create_post_headers(
        token=get_token_fixture,
        user_agent=get_user_agent,
        content_type="application/x-www-form-urlencoded"
    )
    payload = get_create_post_payload(
        subreddit=f"u_{os.getenv('REDDIT_USERNAME')}",
        title="Post sin api_type",
        text="Este post no debería procesarse correctamente"
    )

    # Eliminamos el campo api_type
    payload.pop("api_type", None)
    logger.debug(f"Payload sin api_type: {payload}")
    try:
        assert_payload_matches_schema(payload)
    except AssertionError as e:
        logger.warning(f"Falla del esquema (esperado): {e}")
    response = requests.post(f"{url}/api/submit", headers=headers, data=payload)
    response_json = response.json()
    logger.debug(f"Respuesta JSON al postear sin api_type: {response_json}")

    assert_status_code(response, expected_status=200)
    assert_response_has_errors(response_json)

@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.xfail(reason="BUG-CP009: El servidor deberia aceptar un payload sin 'kind' reportando el error, pero da error 500 internal server error")
def test_CP009_create_post_sin_kind(get_token_fixture, get_user_agent):
    """
    CP-009: Crear post sin campo 'kind'.
    Se espera que la API retorne un error indicando que el campo 'kind' es obligatorio.
    """
    url = "https://oauth.reddit.com"
    headers = get_create_post_headers(
        token=get_token_fixture,
        user_agent=get_user_agent,
        content_type="application/x-www-form-urlencoded"
    )

    payload = get_create_post_payload(
        subreddit=f"u_{os.getenv('REDDIT_USERNAME')}",
        title="Post sin kind",
        text="Contenido no válido"
    )

    # Eliminamos el campo 'kind' para simular el error
    payload.pop("kind", None)
    logger.debug(f"Payload sin kind: {payload}")
    response = requests.post(f"{url}/api/submit", headers=headers, data=payload)
    response_json = response.json()
    logger.debug(f"Respuesta JSON al postear sin kind: {response_json}")

    # Aunque el status sea 200, esperamos que haya errores reportados en la respuesta
    assert_status_code(response, expected_status=200)
    assert_response_has_errors(response_json)

@pytest.mark.functional
@pytest.mark.regression
def test_CP010_create_post_sin_sr(get_token_fixture, get_user_agent):
    """
    CP-010: Crear post sin campo 'sr'.
    Se espera que la API retorne un error indicando que el campo 'sr' (subreddit) es obligatorio.
    """
    url = "https://oauth.reddit.com"
    headers = get_create_post_headers(
        token=get_token_fixture,
        user_agent=get_user_agent,
        content_type="application/x-www-form-urlencoded"
    )

    payload = get_create_post_payload(
        subreddit=f"u_{os.getenv('REDDIT_USERNAME')}",  # Este se eliminará
        title="Post sin sr",
        text="Contenido sin subreddit"
    )

    # Eliminamos el campo 'sr' para simular la omisión del subreddit
    payload.pop("sr", None)
    logger.debug(f"Payload sin subreddit: {payload}")
    response = requests.post(f"{url}/api/submit", headers=headers, data=payload)
    response_json = response.json()
    logger.debug(f"Respuesta JSON al postear sin subreddit: {response_json}")

    # Aunque la API devuelva 200, debe incluir errores en la respuesta
    assert_status_code(response, expected_status=200)
    assert_response_has_errors(response_json)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CP002_create_post_tipo_link_solo_titulo(get_token_fixture, get_user_agent):
    """
    CP-002: Crear post de tipo link solo con título.
    Validar status 200, esquema del payload y respuesta.
    """
    url = "https://oauth.reddit.com"
    headers = get_create_post_headers(
        token=get_token_fixture,
        user_agent=get_user_agent,
        content_type="application/x-www-form-urlencoded"
    )
    payload = get_create_post_payload(
        subreddit=f"u_{os.getenv('REDDIT_USERNAME')}",
        title='En esta ocasión solo el título',
    )

    assert_payload_matches_schema(payload)
    payload.pop("text", None)
    logger.debug(f"Payload para post tipo link solo con título: {payload}")
    response = requests.post(f"{url}/api/submit", headers=headers, data=payload)
    response_json = response.json()
    logger.debug(f"Respuesta JSON al crear post tipo link solo con título: {response_json}")
    # Validaciones
    assert_post_created_successfully(response)
    assert_post_response_schema(response_json)