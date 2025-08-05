import pytest
import logging
import jsonschema
from src.logs.logger import logger
from src.redditApi.reddit_api import obtener_comentarios, obtener_comentario_token_sin_token
from src.assertions.comment_assertions import (
    assert_obtener_comentario,
    assert_existe_body,
    assert_comentario_id_invalido,
    assert_comentario_sin_token
)
from src.schemas.obtener_comentario.obtener_comentario_schema import obtener_comentario_schema

@pytest.mark.functional
@pytest.mark.regression
def test_RC001_obtener_comentario_200():
    """Test para obtener un comentario exitosamente."""
    thing_id = "n6n6i95"  # Reemplaza con un ID de comentario válido
    logger.info("Iniciando test: test_RC001_obtener_comentario_200")
    response = obtener_comentarios(thing_id)
    logger.debug(f"Response: {response}")
    assert_obtener_comentario(response)
    logger.info(f"Status code: {response.status_code}")
    logger.debug(f"Response JSON: {response.json()}")
    jsonschema.validate(instance=response.json(), schema=obtener_comentario_schema)
    logger.info("El esquema de la respuesta es válido.")

@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.xfail(reason="BUG-LC002: Se obtiene un código 200 y en el response no existe el campo error/s")
def test_RC002_obtener_comentario_id_mayuscula():
    """Test para verificar que se maneja un ID de comentario con letras mayúsculas."""
    thing_id = "N6N6I95"
    logger.info("Iniciando test: test_RC002_obtener_comentario_id_mayuscula")
    response = obtener_comentarios(thing_id)
    logger.debug(f"Response: {response}")
    assert_comentario_id_invalido(response)
    logger.info("El ID de comentario con mayúscula se maneja correctamente.")

@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.xfail(reason="BUG-LC004-001: El status code es un 200 y la respuesta no es un JSON válido")
def test_RC003_obtener_comentario_sin_token():
    """Test para verificar que no se permite obtener un comentario sin token de autenticación."""
    thing_id = "n6n6i95"
    logger.info("Iniciando test: test_RC003_obtener_comentario_sin_token")
    response = obtener_comentario_token_sin_token(thing_id)
    logger.debug(f"Response: {response}")
    assert_comentario_sin_token(response)
    logger.info("No se permite obtener comentarios sin token de autenticación.")

@pytest.mark.functional
@pytest.mark.regression
def test_RC004_obtener_comentario_body_existe():
    """Test para verificar que el campo 'body' existe en la respuesta."""
    thing_id = "n6n6i95"
    logger.info("Iniciando test: test_RC004_obtener_comentario_body_existe")
    response = obtener_comentarios(thing_id)
    logger.debug(f"Response: {response}")
    assert_existe_body(response)
    logger.info("El campo 'body' existe y no está vacío.")

@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.xfail(reason="BUG-LC002: Se obtiene un código 200 y en el response no existe el campo error/s")
def test_RC005_obtener_comentario_id_invalido():
    """Test para verificar que se maneja un ID de comentario inválido."""
    thing_id = "invalid_id"
    logger.info("Iniciando test: test_RC005_obtener_comentario_id_invalido")
    response = obtener_comentarios(thing_id)
    logger.debug(f"Response: {response}")
    assert_comentario_id_invalido(response)
    logger.info("El ID de comentario inválido se maneja correctamente.")


#FALTA EL 006 007 008