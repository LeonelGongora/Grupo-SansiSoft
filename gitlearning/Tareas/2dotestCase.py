import requests
import pytest

@pytest.mark.funcional
#prioridad: media
def test404():
    #Titulo:  Validar que la API devuelva 404 al intentar actualizar un objeto inexistente
    #Descripcion: verifica rechace una solicitud PUT cuando se intenta actualizar un objeto con un id que no existe
    url = 'https://api.restful-api.dev/objects/'
    list_url = url + '33'
    body = {
        "name": "Apple MacBook Pro 16\"",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }
    response = requests.put(list_url, json=body)

    assert response.status_code == 404