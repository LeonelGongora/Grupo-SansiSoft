import requests
import pytest
from src.assertions.get_post_assertions import (
    assert_get_post_empty_response,
    assert_status_code
)

@pytest.mark.functional
@pytest.mark.regression
def test_OI004_get_post_id_invalid_format(get_token_fixture):
    """
    OI-004: Obtener información de un post con ID con formato inválido.
    Valida que el status sea 200 y que children esté vacío.
    """
    post_id = "%$######"  # Formato inválido
    url = f"https://oauth.reddit.com/api/info?id={post_id}"
    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        'User-Agent': 'SansiSofRFV/0.1 by IceOld4091'
    }

    response = requests.get(url, headers=headers)
    response_json = response.json()

    # Validar que retorna 200 
    assert_status_code(response, expected_status=200)

    # Validar que children existe y está vacío
    assert_get_post_empty_response(response_json)
