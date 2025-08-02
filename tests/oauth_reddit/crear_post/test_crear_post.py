import requests
import pytest
from src.assertions.post_assertions import assert_post_response_schema, assert_post_created_successfully, assert_payload_matches_schema

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression

def test_CP001_create_post(get_token_fixture, get_user_agent):
    """Descripción: Crea un post exitoso validando status 200 y estructura del payload y respuesta."""
    url = "https://oauth.reddit.com"
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        'User-Agent': get_user_agent,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = {
        'api_type': 'json',
        'sr': 'u_IceOld4091',
        'title': 'Publicacion de prueba con Python con OAuth',
        'kind': 'self',
        'text': 'Esta es la descripcion de una publicación de prueba.',
        'sendreplies': 'true',
        'spoiler': 'false',
        'nsfw': 'false',
        'resubmit': 'true'
    }
      # Validación del payload antes de enviar 
    assert_payload_matches_schema(payload)

    submit_url = f"{url}/api/submit"

    response = requests.post(submit_url, headers=headers, data=payload)
    response_json = response.json()

    # Assertions
    assert_post_created_successfully(response)
    assert_post_response_schema(response_json)