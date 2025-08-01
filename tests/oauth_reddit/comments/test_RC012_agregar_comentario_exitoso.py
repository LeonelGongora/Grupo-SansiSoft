from src.redditApi.reddit_api import comentar_en_post
from src.assertions.comment_assertions import assert_comentario_creado
from src.schemas.crear_comentario.crear_comentario_schema_input import input_schema
from src.schemas.crear_comentario.crear_comentario_output import output_schema

import jsonschema
import pytest
import logging

THING_ID_POST = "t3_1mazjyd"
@pytest.mark.functional
@pytest.mark.smoke
@pytest.mark.regression
def test_RC012_agregar_comentario_exitoso():
    datos_entrada = {
        "thing_id": THING_ID_POST,
        "text": "3ero Comentario de prueba desde test prueba 🚀",
        "api_type": "json",
        "return_rtjson": True
    }

    logging.info("Se va a intentar crear el comentario con el id: %s", THING_ID_POST)
    logging.info("validando los datos de entrada contra el esquema de entrada")
    jsonschema.validate(instance=datos_entrada, schema=input_schema)
    respuesta = comentar_en_post(datos_entrada["thing_id"], datos_entrada["text"])
    wrapped_response = {
        "json": {
            "errors": [],
            "data": {
                "things": [
                    {
                        "kind": "t1",
                        "data": respuesta.json()
                    }
                ]
            }
        }
    }

    jsonschema.validate(instance=wrapped_response, schema=output_schema)
    logging.info("validando la respuesta contra el esquema de salida")
    assert_comentario_creado(wrapped_response,respuesta)