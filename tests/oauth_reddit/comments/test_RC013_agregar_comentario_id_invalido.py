from src.redditApi.reddit_api import comentar_en_post
from src.schemas.crear_comentario.crear_comentario_schema_input import input_schema
from src.schemas.crear_comentario.crear_comentario_output import output_schema
from src.schemas.crear_comentario.crear_comentario_error_schema import error_schema
import jsonschema
import pytest
import logging
THING_ID_INVALIDO = "t3_id_invalido_000"
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.smoke
def test_RC013_agregar_comentario_post_id_invalido():
    datos_entrada = {
        "thing_id": THING_ID_INVALIDO,
        "text": "Comentario con id de post inválido",
        "api_type": "json",
        "return_rtjson": True
    }
    jsonschema.validate(instance=datos_entrada, schema=input_schema)
    logging.info("Se va a intentar crear el comentario con id invalido")
    respuesta = comentar_en_post(datos_entrada["thing_id"], datos_entrada["text"])
    assert respuesta.status_code in [403, 404], f"Se esperaba código 403 o 404, pero fue {respuesta.status_code}"  # se exportaran los asserts
    json_data = respuesta.json()
    jsonschema.validate(instance=json_data, schema=error_schema)
    assert "error" in json_data or "message" in json_data, "No se encontró 'error' o 'message' en la respuesta"