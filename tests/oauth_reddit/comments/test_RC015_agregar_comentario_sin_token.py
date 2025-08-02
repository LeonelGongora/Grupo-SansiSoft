from src.redditApi.reddit_api import comentar_en_post, comentar_en_post_token_erroneo
from src.assertions.comment_assertions import assert_comentario_creado, assert_comentario_sin_token
from src.schemas.crear_comentario.crear_comentario_schema_input import input_schema
from src.schemas.crear_comentario.crear_comentario_output import output_schema

import jsonschema
import pytest
import logging


@pytest.mark.functional
@pytest.mark.smoke
def test_RC015_agregar_comentario_sin_token():
    """Test para agregar un comentario sin token de autenticación."""
    datos_entrada = {
        "thing_id": "t3_1mazjyd",  # ID de un post existente
        "text": "Comentario de prueba sin token 🚫",
        "api_type": "json",
        "return_rtjson": True
    }
    logging.info("Intentando crear un comentario sin token de autenticación.")
    logging.info("Validando los datos de entrada contra el esquema de entrada.")
    jsonschema.validate(instance=datos_entrada, schema=input_schema)
    respuesta = comentar_en_post_token_erroneo(datos_entrada["thing_id"], datos_entrada["text"])
    assert_comentario_sin_token(respuesta)
   