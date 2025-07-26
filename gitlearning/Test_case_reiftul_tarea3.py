import requests

# Prioridad: Alta

def test_RF0004_endpoint_inexistente_objeto():
    """
    El sistema debe devolver un error 404 cuando se accede a un objeto inexistente
    en la API restful-api.dev.
    """
    url = "https://api.restful-api.dev/objects/1234567890abcdef12345678"  # objeto inexistente

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)

    print(f"Response status code: {response.status_code}")
    print(f"Response body: {response.text}")

    # Verificamos que el status code sea 404 Not Found
    assert response.status_code == 404, f"Se esperaba 404, pero se recibió {response.status_code}"
