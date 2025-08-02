import requests
import pytest
from src.assertions.get_post_assertions import (
    assert_get_post_response_schema,
    assert_status_code
)

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

    response = requests.get(url, headers=headers)
    response_json = response.json()

    # Validar que retorna 200
    assert_status_code(response, expected_status=200)

    # Validar que children está vacío
    assert_get_post_response_schema(response_json)
