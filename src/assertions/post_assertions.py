import jsonschema
import json
import os
from src.logs.logger import logger

def assert_payload_matches_schema(payload):
    # Ruta absoluta al archivo de esquema fijo
    base_dir = os.path.dirname(__file__) 
    schema_path = os.path.abspath(os.path.join(base_dir, "../schemas/schemas_post/post_payload_schema.json"))

    with open(schema_path, encoding="utf-8") as f:
        schema = json.load(f)

    jsonschema.validate(instance=payload, schema=schema)

def assert_payload_sin_required_matches_schema(payload):
    # Ruta absoluta al archivo de esquema fijo
    base_dir = os.path.dirname(__file__)
    schema_path = os.path.abspath(os.path.join(base_dir, "../schemas/schemas_post/post_payload_sinRequired_schema.json"))

    with open(schema_path, encoding="utf-8") as f:
        schema = json.load(f)

    jsonschema.validate(instance=payload, schema=schema)

def assert_post_response_schema(response_json):
    # Ruta absoluta al archivo de esquema fijo
    base_dir = os.path.dirname(__file__)
    schema_path = os.path.abspath(os.path.join(base_dir, "../schemas/schemas_post/post_response_schema.json"))

    with open(schema_path, encoding="utf-8") as f:
        schema = json.load(f)
    jsonschema.validate(instance=response_json, schema=schema)

def assert_post_created_successfully(response):
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    assert "json" in response.json()
    logger.debug(response.json())
    assert response.json()["json"]["errors"] == []

def assert_response_has_errors(response_json):
    """
    Valida que la respuesta tenga un campo 'errors' dentro de 'json' y que no esté vacío.
    Lanza una excepción si no cumple estas condiciones.
    """
    assert isinstance(response_json, dict), "La respuesta no es un JSON válido"
    assert "json" in response_json, "La respuesta no contiene el campo 'json'"
    json_data = response_json["json"]

    assert "errors" in json_data, "El campo 'json' no contiene 'errors'"
    assert isinstance(json_data["errors"], list), "'errors' no es una lista"
    assert len(json_data["errors"]) > 0, "La lista de errores está vacía"

