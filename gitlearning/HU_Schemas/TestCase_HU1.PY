import json
import pytest
import requests
import jsonschema

@pytest.mark.smoke
def test_SCRUM_T41_Crear_un_subreddit_con_nombre_valido():
    """
    Verificar que un usuario autenticado pueda crear un subreddit con nombre válido mediante la API de Reddit.
    """

    base_url = "https://oauth.reddit.com"
    endpoint = "/api/site_admin"
    url = base_url + endpoint

    nombresubreddit = "brayandep"
    payload = {
        "name": nombresubreddit.strip(),
        "title": "Subreddit de prueba para QA",
        "public_description": "Este es un subreddit de prueba automatizada",
        "type": "public",
        "link_type": "any",
        "lang": "es",
        "api_type": "json"
    }

    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzUzOTc3NDg4LjYwODA0MiwiaWF0IjoxNzUzODkxMDg4LjYwODA0MiwianRpIjoiS3R2cnJwdzN4UVlWenFCR1VReVFXcTlyaFp5U2d3IiwiY2lkIjoibEc5Y2tPSENZT21vMEVQQ0s3S3pOQSIsImxpZCI6InQyX2NpbW9jNnJ2IiwiYWlkIjoidDJfY2ltb2M2cnYiLCJsY2EiOjE2MjI3ODAxNzQwMDAsInNjcCI6ImVKeUtWdEpTaWdVRUFBRF9fd056QVNjIiwiZmxvIjo5fQ.S4uin8INoH2odtweL8DfS35lBXCalsfWM2u-clGcZP2pyIAEoaVKo3A_DVbXyW-ZXpoD00WY3YryQATu0r4WGcsSmoeDl_lvUzxoSowq6FuPwzKRDoy0qwkm4yHFMfybY19UGuMP9mT1yy5AiFLYLp2oX9Nyn8_A1zOfi8IBZ0tXWcB9mXW57GwmH6tQIb8YPKTYTjfT170lwhZ13ONshp0Dy-whYGJ7OeM5K7PKIXhuWmscyo8Kd068ziHyHYbr9Lv8ij43SQ--Vxj8f2x-MEbMJj5hBLd7PjlP3aed3IeJ30GA7s9RmGaOs_8d_VyCcRMNZa0sIRCOJ27PFUai2g",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "MiScriptQA/0.1"
    }

    response = requests.post(url, headers=headers, data=payload)

    print(response.status_code)
    print(response.text)

    assert response.status_code == 200, "No se pudo crear el subreddit"

    # Validación de esquema simple
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "json": {
                "type": "object",
                "properties": {
                    "errors": {
                        "type": "array",
                        "items": {}
                    }
                },
                "required": ["errors"]
            }
        },
        "required": ["json"]
    }

    try:
        jsonschema.validate(instance=response.json(), schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema no coincide: {err}")
