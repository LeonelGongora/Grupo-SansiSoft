import requests

# Prioridad
# Alta

def test_RF0004_endpoint_inexistente_de_noticias():
    """El sistema debe devolver un error 404 cuando se accede a un endpoint inexistente en la API de The Guardian."""

    url = "https://content.guardianapis.com/searchX?page=2&q=debate&api-key=test"  # endpoint inválido

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)

    assert response.status_code == 404
