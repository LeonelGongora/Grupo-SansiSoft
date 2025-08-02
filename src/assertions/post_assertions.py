import jsonschema
import json
import os


def assert_payload_matches_schema(payload):
    # Ruta absoluta al archivo de esquema fijo
    base_dir = os.path.dirname(__file__)  # src/assertions/
    schema_path = os.path.abspath(os.path.join(base_dir, "../resources/payloads/post_payload_schema.json"))

    with open(schema_path, encoding="utf-8") as f:
        schema = json.load(f)

    jsonschema.validate(instance=payload, schema=schema)

def assert_post_response_schema(response_json):
    # Ruta absoluta al archivo de esquema fijo
    base_dir = os.path.dirname(__file__)  # src/assertions/
    schema_path = os.path.abspath(os.path.join(base_dir, "../resources/schemas/post_response_schema.json"))

    with open(schema_path, encoding="utf-8") as f:
        schema = json.load(f)
    jsonschema.validate(instance=response_json, schema=schema)

def assert_post_created_successfully(response):
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    assert "json" in response.json()
    print(response.json()["json"]["errors"])
    assert response.json()["json"]["errors"] == []

