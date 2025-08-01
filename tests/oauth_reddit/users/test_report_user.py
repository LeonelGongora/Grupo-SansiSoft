import os
import requests
import jsonschema
import pytest
import json
import pytest

@pytest.mark.smoke
@pytest.mark.functional
def test_OI_003_reportar_usuario_exitosamente(get_token_fixture):
    """ Descripcion Se reporta a un usuario registrado en Reddit, utilizando su nombre de usuario e indicando un motivo"""

    access_token = get_token_fixture
    url = "https://oauth.reddit.com/api/report_user"
    headers = {
        "Authorization": f"bearer {access_token}",
        "User-Agent": os.getenv("REDDIT_USER_AGENT"),
        "Content-Type": "application/json"
    }
    data = {
        "user": os.getenv("REDDIT_USERNAME_VALIDO"),
        "reason" : "Este es el motivo"
    }

    base_direccion = os.path.dirname(__file__) 
    schema_path = os.path.abspath(os.path.join(base_direccion, "../../../src/resources/schemas/post_input_report_user_schema.json"))

    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    try:
        jsonschema.validate(data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide: {err}")

    response = requests.post(url, headers=headers, json=data)

    assert response.status_code == 200

    base_direccion1 = os.path.dirname(__file__) 
    schema_path = os.path.abspath(os.path.join(base_direccion1, "../../../src/resources/schemas/post_response_report_user_schema.json"))

    with open(schema_path, "r", encoding="utf-8") as f:
        schema1 = json.load(f)

    try:
        jsonschema.validate(response.json(), schema=schema1)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide:{err}")
