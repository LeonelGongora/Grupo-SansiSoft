import jsonschema
from jsonschema import validate
from src.schemas.subreddit.subreddit_schema_output import output_schema

subreddit_response_schema = {
    "type": "object",
    "properties": {
        "kind": {"type": "string"},
        "data": {
            "type": "object",
            "properties": {
                "display_name": {"type": "string"},
                "subreddit_type": {"type": "string"},
                "title": {"type": "string"},
                "description": {"type": "string"},
            },
            "required": ["display_name"]
        }
    },
    "required": ["kind", "data"]
}

def assert_subreddit_creado_exitosamente(response_json):
    if "json" not in response_json:
        raise AssertionError(f"❌ No se encontró el campo 'json' en la respuesta: {response_json}")
    
    errors = response_json["json"].get("errors", [])
    assert errors == [], f"❌ Errores detectados al crear el subreddit: {errors}"
    
    print("✅ Subreddit creado exitosamente sin errores.")

def assert_subreddit_schema_output(response_json):
    try:
        jsonschema.validate(instance=response_json, schema=output_schema)
        print("✅ La respuesta cumple con el esquema de salida esperado.")
    except jsonschema.exceptions.ValidationError as e:
        raise AssertionError(f"❌ Validación contra esquema de salida fallida: {e}")

def assert_subreddit_created_successfully(response):
    assert response.status_code == 200, f"❌ Esperado 200, recibido {response.status_code}"

    json_response = response.json()
    assert "data" in json_response, "❌ La respuesta no contiene la clave 'data'"
    assert "display_name" in json_response["data"], "❌ Falta 'display_name' en 'data'"

    print(f"✅ Subreddit creado correctamente con display_name: {json_response['data']['display_name']}")

def assert_subreddit_response_schema(json_response):
    try:
        validate(instance=json_response, schema=subreddit_response_schema)
        print("✅ La respuesta cumple con el esquema general de subreddit.")
    except jsonschema.exceptions.ValidationError as e:
        raise AssertionError(f"❌ La respuesta no cumple con el esquema de subreddit: {e}")
