import pytest
import requests

@pytest.mark.smoke
def test_US001_Verificar_que_no_se_permita_actualizar_el_usuario_de_id_10():

    """Descripción: El usuario no puede  actualizar los datos del celular de id 10"""

    url = "https://api.restful-api.dev/"
    list_url=url+"objects?id=3&id=5&id=10"
    response = requests.put(list_url)
    assert response.status_code == 405