import requests

# Prioridad
# Alta

def test_case_Obtener_objeto():
    """ El usuario debe poder obtener la información de un post específico mediante su ID especifico. """

    url = "https://api.restful-api.dev/objects?id=ff8081819782e69e019858745c0f0c89"

    headers = {}

    response = requests.get(url, headers=headers)

    assert response.status_code == 200, "El código de estado esperado es 200 OK"