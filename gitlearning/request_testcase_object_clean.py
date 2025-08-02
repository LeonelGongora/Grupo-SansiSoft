import pytest
import requests

@pytest.mark.smoke
def test_US001_Obtener_los_datos_de_celular_con_id_de_10():

    """Descripción: El usuario puede obtener los datos de celulares con su nombre, "id", "name", "data", "Capacity", "Screen size"""""

    url = "https://api.restful-api.dev/"
    list_url=url+"objects?id=3&id=5&id=10"
    response = requests.get(list_url)
    assert response.status_code == 200




