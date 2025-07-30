import json
import pytest
import requests
import jsonschema

@pytest.mark.smoke
def test_004_T41_Crear_una_publicacion():
    """
    Verificar que se cree una publicacion.
    """

    base_url = "https://jsonplaceholder.typicode.com"
    endpoint = "/posts"
    url = base_url + endpoint

    payload = {
        "title": "Mi nuevo post 10",
        "body": "Este es el contenido del post",
        "userId": 1
    }

    headers = {
        "Content-Type": "application/json"
    }


    response = requests.post(url, headers=headers, json=payload)

    print(response.status_code)
    print(response.text)

    assert response.status_code == 201, "No se pudo crear la publicación"  # 201 es lo correcto


    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "title": { "type": "string" },
            "body": { "type": "string" },
            "userId": { "type": "integer" },
            "id": { "type": "integer" }
        },
        "required": ["title", "body", "userId", "id"]
    }

    try:
        jsonschema.validate(instance=response.json(), schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema no coincide: {err}")