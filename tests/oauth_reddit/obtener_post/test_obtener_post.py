import requests
import pytest
from src.assertions.get_post_assertions import assert_get_post_response_schema, assert_status_code

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CP002_get_post_by_id(get_token_fixture, created_post_id):
    """Descripción: Consulta un post por ID validando status 200 y la estructura de la respuesta."""

    post_id = created_post_id
    url = f"https://oauth.reddit.com/api/info?id={post_id}"
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        'User-Agent': 'SansiSofRFV/0.1 by IceOld4091'
    }

    response = requests.get(url, headers=headers)
    response_json = response.json()

    # Validaciones
    assert_status_code(response, expected_status=200)
    assert_get_post_response_schema(response_json)
