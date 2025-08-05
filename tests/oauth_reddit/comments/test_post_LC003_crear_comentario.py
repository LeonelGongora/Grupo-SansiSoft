import pytest
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
from src.logs.logger import logger

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
    logger.info("🚀 Test RC012 - Crear comentario exitoso.")
    logger.debug(f"Datos de entrada: {datos_entrada}")
    jsonschema.validate(instance=datos_entrada, schema=input_schema)
    respuesta = comentar_en_post(datos_entrada["thing_id"], datos_entrada["text"])
    logger.debug(f"Respuesta JSON: {respuesta.json()}")
    jsonschema.validate(instance=respuesta.json(), schema=schema_data)
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
    logger.info("❌ Test RC013 - Comentario con ID de post inválido.")
    logger.debug(f"Datos de entrada: {datos_entrada}")
    jsonschema.validate(instance=datos_entrada, schema=input_schema)
    respuesta = comentar_en_post(datos_entrada["thing_id"], datos_entrada["text"])
    logger.debug(f"Status code: {respuesta.status_code}")
    logger.debug(f"Respuesta JSON: {respuesta.json()}")
    assert respuesta.status_code in [403, 404], f"Se esperaba código 403 o 404, pero fue {respuesta.status_code}"
    jsonschema.validate(instance=respuesta.json(), schema=error_schema)
    assert "error" in respuesta.json() or "message" in respuesta.json(), "No se encontró 'error' o 'message' en la respuesta"


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
    logger.info("🟢 Test RC014 - Verificación de código 200 en comentario exitoso.")
    logger.debug(f"Datos de entrada: {datos_entrada}")
    respuesta = comentar_en_post(datos_entrada["thing_id"], datos_entrada["text"])
    logger.debug(f"Status code: {respuesta.status_code}")
    assert respuesta.status_code == 200, f"Esperado código 200, obtenido {respuesta.status_code}"


@pytest.mark.functional
@pytest.mark.smoke
def test_RC015_agregar_comentario_sin_token():
    datos_entrada = {
        "thing_id": "t3_1mazjyd",
        "text": "Comentario de prueba sin token 🚫",
        "api_type": "json",
        "return_rtjson": True
    }
    logger.info("🔒 Test RC015 - Comentario sin token de autenticación.")
    logger.debug(f"Datos de entrada: {datos_entrada}")
    jsonschema.validate(instance=datos_entrada, schema=input_schema)
    respuesta = comentar_en_post_token_erroneo(datos_entrada["thing_id"], datos_entrada["text"])
    logger.debug(f"Respuesta JSON: {respuesta.json()}")
    assert_comentario_sin_token(respuesta)


@pytest.mark.functional
@pytest.mark.smoke
def test_RC017_agregar_comentario_token_caducado():
    datos_entrada = {
        "thing_id": "t3_1mazjyd",
        "text": "Comentario de prueba con token caducado 🚫",
        "api_type": "json",
        "return_rtjson": True
    }
    logger.info("⏳ Test RC017 - Comentario con token caducado.")
    logger.debug(f"Datos de entrada: {datos_entrada}")
    jsonschema.validate(instance=datos_entrada, schema=input_schema)
    respuesta = comentar_en_post_token_caducado(datos_entrada["thing_id"], datos_entrada["text"])
    logger.debug(f"Respuesta JSON: {respuesta.json()}")
    assert_comentario_token_caducado(respuesta)


def test_RC018_campos_requeridos_en_payload_comentario():
    logger.info("🧪 Test RC018 - Validar campos requeridos en payload del comentario.")
    payload_valido = crear_payload_comentario("t3_1mazjyd", "Texto de prueba")
    campos_requeridos = list(payload_valido.keys())

    for campo in campos_requeridos:
        payload_invalido = payload_valido.copy()
        del payload_invalido[campo]
        logger.debug(f"Validando sin el campo: {campo} -> Payload: {payload_invalido}")
        with pytest.raises(jsonschema.exceptions.ValidationError) as exc_info:
            jsonschema.validate(instance=payload_invalido, schema=input_schema)
        logger.info(f"Campo faltante: {campo} => Error: {exc_info.value.message}")


@pytest.mark.parametrize("texto", ["", " "])
def test_RC020_comentario_vacio_o_espacios(texto):
    datos_entrada = {
        "thing_id": THING_ID_POST,
        "text": texto,
        "api_type": "json",
        "return_rtjson": True
    }
    logger.info("🧪 Test RC020 - Comentario vacío o con solo espacios.")
    logger.debug(f"Datos de entrada: {datos_entrada}")
    jsonschema.validate(instance=datos_entrada, schema=input_schema)
    respuesta = comentar_en_post(datos_entrada["thing_id"], datos_entrada["text"])
    logger.debug(f"Respuesta JSON: {respuesta.json()}")
    assert_comentario_vacio_espacios(respuesta)
