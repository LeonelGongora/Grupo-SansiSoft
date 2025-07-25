import requests

# Prioridad
# Alta

def test_RF0002_crear_objeto_con_json_invalido():
    """El sistema debe devolver un error 400 cuando se intenta crear un objeto con JSON mal formado."""

    url = "https://api.restful-api.dev/objects"

    headers = {
        'Content-Type': 'application/json'
    }

    # JSON mal formado: falta una coma entre "name" y "data"
    payload = '''
    {
        "name": "Nombre 5"
        "data": {}
    }
    '''

    response = requests.post(url, headers=headers, data=payload)

    assert response.status_code == 400
