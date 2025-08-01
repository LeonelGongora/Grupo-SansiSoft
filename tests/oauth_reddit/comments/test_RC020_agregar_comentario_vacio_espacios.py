from src.redditApi.reddit_api import comentar_en_post
from src.assertions.comment_assertions import assert_comentario_vacio_espacios
from src.schemas.crear_comentario.crear_comentario_schema_input import input_schema
from src.schemas.crear_comentario.crear_comentario_output import output_schema
from src.schemas.crear_comentario.crear_comentario_error_schema import error_schema
import jsonschema
import pytest
import logging

THING_ID_POST = "t3_1mazjyd"

@pytest.mark.parametrize("texto", ["", " "])
def test_RC020_comentario_vacio_o_espacios(texto):
    datos_entrada = {
        "thing_id": THING_ID_POST,
        "text": texto,
        "api_type": "json",
        "return_rtjson": True
    }
    logging.info("Se va a intentar crear el comentario inválido ('%s') con el id: %s", texto, THING_ID_POST)
    logging.info("Validando los datos de entrada contra el esquema de entrada")

    jsonschema.validate(instance=datos_entrada, schema=input_schema)
    respuesta = comentar_en_post(datos_entrada["thing_id"], datos_entrada["text"])
    assert_comentario_vacio_espacios(respuesta)