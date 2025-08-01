import jsonschema
import json
import os
import requests
def get_schema(relative_path):
    base_dir = os.path.dirname(__file__)  # src/assertions/
    schema_path = os.path.abspath(os.path.join(base_dir, relative_path))
    with open(schema_path, encoding="utf-8") as f:
        schema = json.load(f)
    return schema

def assert_add_friend_success_payload_schema(payload):
    schema = get_schema("../resources/payloads/amigo_payload_success_schema.json")
    jsonschema.validate(instance=payload, schema=schema)
    print("\n  Datos de solicitud correctos")

def assert_add_friend_success_response_schema(response_json):
    schema = get_schema("../resources/schemas/amigo_response_success_schema.json")
    jsonschema.validate(instance=response_json, schema=schema)
    print("\n✅ Respuesta esperada")
def assert_add_friend_successfully(response):
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    print("\n✅ Retorna esperado codigo 200")
