import requests

def test_NJTD02_crear_objeto_con_json_invalido():
    """
    Validar que la API devuelve un error 4xx al enviar un JSON mal formado al crear un objeto.
    """
    url = "https://api.restful-api.dev/objects"
    headers = {
        'Content-Type': 'application/json'
    }

    # JSON mal formado: falta una coma entre "name" y "data"
    invalid_json_payload = '''
    {
        "name": "Nombre 5"
        "data": {}
    }
    '''  # Falta la coma después de "Nombre 5"

    response = requests.post(url, headers=headers, data=invalid_json_payload)

    print(f"Response status code: {response.status_code}")
    print(f"Response body: {response.text}")

    # Se espera un código de error cliente (4xx)
    assert 400 <= response.status_code < 500, \
        f"Se esperaba un error cliente 4xx, pero se obtuvo {response.status_code}"
