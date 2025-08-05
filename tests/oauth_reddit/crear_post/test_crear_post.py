import requests
import pytest
import os
from dotenv import load_dotenv
load_dotenv()
from src.assertions.post_assertions import assert_post_response_schema, assert_post_created_successfully, assert_payload_matches_schema
from src.payloads.payload_crear_post import get_create_post_payload

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.ejecutar
def test_CP001_create_post_exitoso(get_token_fixture, get_user_agent):
    """Descripción: Crea un post exitoso validando status 200 y la estructura del payload y respuesta."""
    url = "https://oauth.reddit.com"
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        'User-Agent': get_user_agent,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
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

    # Assertions
    assert_post_created_successfully(response)
    assert_post_response_schema(response_json)