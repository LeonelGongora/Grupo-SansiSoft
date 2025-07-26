import pytest
import requests

@pytest.mark.smoke
def test_US001_Verificar_que_no_se_permita_llamar_al_id_11213165():

    """Descripción: El usuario no puede  obtener los datos del id=11213165 por que no existe"""

    url = "https://api.restful-api.dev/"
    list_url=url+"objects/11213165"
    response = requests.get(list_url)
    assert response.status_code == 404