import pytest
import logging
import jsonschema

from src.redditApi.reddit_api import (
    comentar_en_post,
    comentar_en_post_token_erroneo,
    comentar_en_post_token_caducado
)

from src.assertions.comment_assertions import (
    assert_comentario_creado,
    assert_comentario_sin_token,
    assert_comentario_token_caducado,
    assert_comentario_vacio_espacios
)

from src.schemas.crear_comentario.crear_comentario_schema_input import input_schema
from src.schemas.crear_comentario.crear_comentario_output import output_schema
from src.schemas.crear_comentario.crear_comentario_output_exitoso import schema_data
from src.schemas.crear_comentario.crear_comentario_error_schema import error_schema
from src.payloads.comment_payload import crear_payload_comentario

THING_ID_POST = "t3_1mf10gx"
THING_ID_INVALIDO = "t3_invalid_id"
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
    logging.info("validando que se haya creado el comentario exitosamente")
    jsonschema.validate(instance=respuesta.json(), schema=schema_data)
    logging.info("validando la respuesta contra el esquema de salida")
    assert_comentario_creado(respuesta.json())



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

@pytest.mark.functional
@pytest.mark.smoke
@pytest.mark.regression
def test_RC014_codigo_200_comentario_usuario_valido():
    datos_entrada = {
        "thing_id": THING_ID_POST,
        "text": "Comentario para verificar código 200",
        "api_type": "json",
        "return_rtjson": True
    }
    logging.info("Intentando crear comentario para verificar código 200 con id: %s", THING_ID_POST)
    respuesta = comentar_en_post(datos_entrada["thing_id"], datos_entrada["text"])
    logging.info("Validando que el código HTTP sea 200")
    assert respuesta.status_code == 200, f"Esperado código 200, obtenido {respuesta.status_code}"
    logging.info("✅ Código 200 recibido correctamente al comentar con usuario válido.")

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

@pytest.mark.functional
@pytest.mark.smoke
def test_RC017_agregar_comentario_token_caducado():
    """Test para agregar un comentario con token de autenticación caducado."""
    datos_entrada = {
        "thing_id": "t3_1mazjyd",  # ID de un post existente
        "text": "Comentario de prueba con token caducado 🚫",
        "api_type": "json",
        "return_rtjson": True
    }
    logging.info("Intentando crear un comentario con token de autenticación caducado.")
    logging.info("Validando los datos de entrada contra el esquema de entrada.")
    jsonschema.validate(instance=datos_entrada, schema=input_schema)
    respuesta = comentar_en_post_token_caducado(datos_entrada["thing_id"], datos_entrada["text"])
    assert_comentario_token_caducado(respuesta)

def test_RC018_campos_requeridos_en_payload_comentario():
    payload_valido = crear_payload_comentario("t3_1mazjyd", "Texto de prueba")
    logging.info("Validando los campos requeridos en el payload de comentario")
    campos_requeridos = list(payload_valido.keys())
    for campo in campos_requeridos:
        payload_invalido = payload_valido.copy()
        del payload_invalido[campo]

        with pytest.raises(jsonschema.exceptions.ValidationError) as exc_info:
            jsonschema.validate(instance=payload_invalido, schema=input_schema)

        print(f"Campo faltante: {campo} => Error: {exc_info.value.message}")


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