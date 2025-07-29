import requests

# Prioridad
# Alta

def test_RFVObtenerObject():
    """
    El usuario debe poder obtener la información de un post específico mediante su ID.
    """

    url = "https://api.restful-api.dev/objects?id=ff8081819782e69e019839a42b43708c"

    headers = {}

    response = requests.get(url, headers=headers)

    assert response.status_code == 200, "El código de estado esperado es 200 OK"

