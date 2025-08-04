import jsonschema
import json
import os
from jsonschema import validate

def assert_payload_matches_schema(payload):
    # Ruta absoluta al archivo de esquema fijo
    base_dir = os.path.dirname(__file__)  # src/assertions/
    schema_path = os.path.abspath(os.path.join(base_dir, "../schemas/suscribirse_a_sr/post_suscribirse_payload_schema.json"))
    with open(schema_path, encoding="utf-8") as f:
        schema = json.load(f)
    jsonschema.validate(instance=payload, schema=schema)

def assert_suscribirse_response_schema(response_json):
    # Ruta absoluta al archivo de esquema fijo
    base_dir = os.path.dirname(__file__)  # src/assertions/
    schema_path = os.path.abspath(os.path.join(base_dir, "../schemas/suscribirse_a_sr/post_suscribirse_response_schema.json"))
    with open(schema_path, encoding="utf-8") as f:
        schema = json.load(f)
    jsonschema.validate(instance=response_json, schema=schema)

def assert_post_created_successfully(response):#respuesta normal de exito
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    assert "json" in response.json()
    assert response.json()["json"]["errors"] == []


def assert_subscribe_success_empty_response(response):#para respuesta vacia {}
    assert response.status_code == 200
    assert response.json() == {}

def assert_response_unauthorized(response):
    assert response.status_code == 401, f"Expected 401 but got {response.status_code}"
    assert "unauthorized" in response.text.lower() or "not found" in response.text.lower()

def assert_response_bad_request(response):
    assert response.status_code == 400, f"Expected 400 but got {response.status_code}"
    assert "error" in response.text.lower() or "bad request" in response.text.lower()


def assert_response_forbidden(response):
    assert response.status_code == 403, f"Expected 403 but got {response.status_code}"

    # Convertir el body a texto plano y pasarlo a minúsculas
    response_text = response.text.lower()

    # Lista de palabras aceptadas
    palabras_clave = ["forbidden", "blocked", "sign in"]

    # Verificar que al menos una palabra esté presente
    assert any(palabra in response_text for palabra in palabras_clave), (
        f"Ninguna de las palabras clave esperadas se encontró en la respuesta 403: {palabras_clave}"
    )

def assert_response_not_found(response):
    assert response.status_code == 404, f"Expected 404 but got {response.status_code}"
    assert "not found" in response.text.lower()


def assert_response_conflict(response):
    assert response.status_code == 409, f"Expected 409 but got {response.status_code}"
    assert "conflict" in response.text.lower() or "already" in response.text.lower() or "subscribed" in response.text.lower(), \
        f"Expected conflict-related message in response, got: {response.text}"
def assert_response_too_many_requests(response):
    assert response.status_code == 429, f"Expected 429 but got {response.status_code}"
    assert "too many requests" in response.text.lower() or "rate limit" in response.text.lower(), \
        f"Expected rate-limit related message in response, got: {response.text}"

def assert_special_jquery_error_schema(response):#Respuesta especial
    # Verificar que el código de estado sea 200 (aunque sea un error lógico para nosotros)
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

    # Validar el cuerpo con el esquema
    schema_path = os.path.join(os.path.dirname(__file__),
                               "../resources/schemas/post_suscribirse_response_schema_special.json")
    with open(schema_path, "r") as f:
        schema = json.load(f)

    response_json = response.json()
    validate(instance=response_json, schema=schema)

def assert_payloadsinaction_matches_schema(payload):
    # Ruta absoluta al archivo de esquema fijo
    base_dir = os.path.dirname(__file__)  # src/assertions/
    schema_path = os.path.abspath(os.path.join(base_dir, "../schemas/suscribirse_a_sr/schema_suscribirse_sin_action.json"))
    with open(schema_path, encoding="utf-8") as f:
        schema = json.load(f)
    jsonschema.validate(instance=payload, schema=schema)
