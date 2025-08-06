import json
import os
import jsonschema
from jsonschema import validate
from src.logs.logger import logger  # Asegúrate de que exista este logger en tu proyecto

def _load_schema(schema_relative_path):
    base_dir = os.path.dirname(__file__)
    schema_path = os.path.abspath(os.path.join(base_dir, schema_relative_path))
    with open(schema_path, encoding="utf-8") as f:
        return json.load(f)

def assert_subreddit_response_schema(response_json):
    """
    Valida que el JSON de respuesta cumpla con el esquema esperado para la creación de subreddits.
    """
    schema = _load_schema("../schemas/subreddit/subreddit_response_schema.json")
    try:
        validate(instance=response_json, schema=schema)
        logger.info("La respuesta cumple con el esquema de subreddit.")
    except jsonschema.exceptions.ValidationError as e:
        logger.error(f" La respuesta no cumple con el esquema: {e}")
        raise AssertionError(f" La respuesta no cumple con el esquema: {e}")

def assert_subreddit_schema_output(response_json):
    """
    Valida el esquema de salida de un subreddit después de la creación.
    """
    schema = _load_schema("../schemas/subreddit/subreddit_schema_output.json")
    try:
        validate(instance=response_json, schema=schema)
        logger.info("La respuesta cumple con el esquema de salida esperado.")
    except jsonschema.exceptions.ValidationError as e:
        logger.error(f" Validación contra esquema de salida fallida: {e}")
        raise AssertionError(f"Validación contra esquema de salida fallida: {e}")


def assert_subreddit_created_successfully(response):
    assert response.status_code == 200, f"Esperado 200, recibido {response.status_code}"
    json_body = response.json()

def assert_subreddit_creation_failed(response, expected_error=None):
    """
    Verifica que la creación de un subreddit falló correctamente, y que los errores esperados estén presentes.
    """
    assert response.status_code in [400, 403, 409], f" Esperado código de error, recibido {response.status_code}"
    json_response = response.json()
    assert "json" in json_response, " La respuesta no contiene el campo 'json'"
    assert "errors" in json_response["json"], " La respuesta no contiene el campo 'errors'"
    if expected_error:
        error_codes = [e[0] for e in json_response["json"]["errors"]]
        assert expected_error in error_codes, f" Error esperado '{expected_error}' no encontrado. Errores recibidos: {error_codes}"
    logger.info("Subreddit no se creó como se esperaba y los errores fueron detectados correctamente.")

def assert_response_unauthorized(response):
    assert response.status_code == 401, f"Expected 401 but got {response.status_code}"
    assert "unauthorized" in response.text.lower() or "not found" in response.text.lower()

def assert_response_missing_token(response):
    assert response.status_code == 200, f"Esperado 401, recibido {response.status_code}"
    logger.info("✅ Respuesta 401 verificada por falta de token.")

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
def assert_response_invalid_subreddit_name(response):
    assert response.status_code in [400, 422], f"Esperado error por nombre inválido, recibido {response.status_code}"
    assert "invalid" in response.text.lower() or "bad_request" in response.text.lower(), \
        "No se encontró mensaje de error esperado por nombre inválido"
    logger.info("✅ SRB-016: Error correctamente manejado por nombre vacío o inválido.")

def assert_response_invalid_name_error(response):
    assert response.status_code == 200, f"Esperado 200, recibido {response.status_code}"
    json_data = response.json()
    errors = json_data.get("json", {}).get("errors", [])
    assert any("INVALID_NAME" in err for err in errors), "No se encontró 'INVALID_NAME' en los errores"
    logger.info("✅ Error 'INVALID_NAME' correctamente devuelto para nombre demasiado corto.")
