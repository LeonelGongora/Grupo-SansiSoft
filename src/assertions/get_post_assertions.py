import jsonschema
import json
import os

def assert_get_post_response_schema(response_json):
    # Ruta absoluta al archivo de esquema fijo
    base_dir = os.path.dirname(__file__)  # src/assertions/
    schema_path = os.path.abspath(os.path.join(base_dir, "../schemas/schemas_post/get_post_response_schema.json"))


    with open(schema_path, encoding="utf-8") as f:
        schema = json.load(f)
    jsonschema.validate(instance=response_json, schema=schema)

def assert_get_post_empty_response(response_json):
    """Valida que children esté vacío."""
    assert "data" in response_json, "La clave 'data' no está en la respuesta"
    assert isinstance(response_json["data"].get("children"), list), "children no es una lista"
    assert response_json["data"]["children"] == [], "children debe estar vacío para ID inexistente"


def assert_status_code(response, expected_status=200):
    actual_status = response.status_code
    assert actual_status == expected_status, f"Expected {expected_status} but got {actual_status}"

def assert_required_post_fields_present(response_json):
    """
    Verifica que los campos requeridos estén presentes.
    Campos requeridos: subreddit, author_fullname, title, id, url
    """
    children = response_json.get("data", {}).get("children", [])
    assert children, "La respuesta no contiene posts en 'children'"

    post_data = children[0].get("data", {})
    required_fields = ["subreddit", "author_fullname", "title", "id", "url"]

    for field in required_fields:
        assert field in post_data, f"Falta el campo requerido: {field}"
        assert post_data[field] is not None, f"El campo {field} está presente pero es None"


