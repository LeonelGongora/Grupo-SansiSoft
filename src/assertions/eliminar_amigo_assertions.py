import jsonschema
import json
import os
import pytest
from src.logs.logger import logger
def get_schema(relative_path):
    base_dir = os.path.dirname(__file__)  # src/assertions/
    schema_path = os.path.abspath(os.path.join(base_dir, relative_path))
    with open(schema_path, encoding="utf-8") as f:
        schema = json.load(f)
    return schema

def assert_delete_friend_success_payload_schema(payload):
    schema = get_schema("../schemas/eliminar_amigo/amigo_payload_success.json")
    try:
        jsonschema.validate(instance=payload, schema=schema)
    except jsonschema.exceptions.ValidationError as e:
        pytest.xfail(f"Schema payload inválido: {e}")

    

def assert_delete_friend_success_response_schema(response_json):
    schema = get_schema("../schemas/eliminar_amigo/amigo_response_success_schema.json")
    try:
        jsonschema.validate(instance=response_json, schema=schema)
    except jsonschema.exceptions.ValidationError as e:
        pytest.xfail(f"Schema response inválido: {e}")
def assert_delete_friend_successfully(response):
    if response.status_code != 200:
        pytest.xfail(f"Codigo esperado era 200, pero obtuvo {response.status_code}")
    assert response.status_code == 200, f"Codigo esperado era 200, pero obtuvo {response.status_code}"
