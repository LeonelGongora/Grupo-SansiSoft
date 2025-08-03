import requests
import pytest
from src.assertions.post_assertions import assert_post_response_schema, assert_post_created_successfully, assert_payload_matches_schema
from os import getenv
@pytest.mark.smoke
@pytest.mark.functional

@pytest.mark.ejecutar
def test_CP001_create_post(get_token_fixture):
    """Descripción: Crea un post exitoso validando status 200 y estructura del payload y respuesta."""
    url = "https://oauth.reddit.com"
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        'User-Agent': f'{getenv("REDDIT_USER_AGENT")}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = {
        'api_type': 'json',
        'sr': f'u_{getenv("REDDIT_SUBREDDIT")}',
        'title': 'Publicacion de prueba con Python con OAuth desde Codigo',
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
    print(response_json["json"]["data"]["url"])
    assert_post_response_schema(response_json)
