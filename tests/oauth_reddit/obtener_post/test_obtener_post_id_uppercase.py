import requests
import pytest
from src.assertions.get_post_assertions import (
    assert_get_post_empty_response,
    assert_status_code
)

@pytest.mark.functional
@pytest.mark.regression
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

    response = requests.get(url, headers=headers)
    response_json = response.json()

    # Validar que retorna 200
    assert_status_code(response, expected_status=200)

    # Validar que children está vacío
    assert_get_post_empty_response(response_json)
