import requests
import pytest
from src.assertions.get_post_assertions import (
    assert_get_post_empty_response,
    assert_status_code
)

@pytest.mark.functional
@pytest.mark.regression
def test_OI006_get_post_without_query_params(get_token_fixture):
    """
    OI-006: Obtener información de un post sin incluir query params.
    Valida que el status sea 200 y que children esté vacío.
    """
    url = "https://oauth.reddit.com/api/info"  # Sin parámetros
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
