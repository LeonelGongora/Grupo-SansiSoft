import json
import requests
import pytest
import sys
import os
from dotenv import load_dotenv
import jsonschema

load_dotenv()

@pytest.mark.smoke
@pytest.mark.functional
def test_OI_001_obtener_info_usuario_existente(get_token_fixture):

    """Descripción: Se obtiene la informacion de un usuario, utilizando un nombre de usuario existente"""

    username_objetivo = os.getenv("REDDIT_USERNAME_VALIDO")# Usuario existente
    access_token = get_token_fixture 

    headers = {
        "Authorization": f"bearer {access_token}",
        "User-Agent": os.getenv("REDDIT_USER_AGENT")
    }

    url = f"https://oauth.reddit.com/user/{username_objetivo}/about"
    response = requests.get(url, headers=headers)

    assert response.status_code == 200

    base_direccion = os.path.dirname(__file__) 
    schema_path = os.path.abspath(os.path.join(base_direccion, "../../../src/resources/schemas/get_user_info_response_schema.json"))

    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    try:
        jsonschema.validate(instance=response.json(), schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide {err}")
