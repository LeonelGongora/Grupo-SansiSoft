import pytest
import logging
import jsonschema
from src.redditApi.reddit_api import obtener_comentarios,obtener_comentario_token_sin_token
from src.assertions.comment_assertions import assert_obtener_comentario, assert_existe_body, assert_comentario_id_invalido,assert_comentario_sin_token
from src.schemas.crear_comentario.obtener_comentario_schema import obtener_comentario_schema





@pytest.mark.functional
@pytest.mark.regression
def test_RC001_obtener_comentario_200():
    """Test para obtener un comentario exitosamente."""
    thing_id = "n6n6i95"  # Reemplaza con un ID de comentario válido
    response = obtener_comentarios(thing_id)
    logging.info("Validando que se haya obtenido el comentario exitosamente")
    assert_obtener_comentario(response)
    jsonschema.validate(instance=response.json(),schema=obtener_comentario_schema)
    logging.info("El esquema de la respuesta es valido")



@pytest.mark.functional
@pytest.mark.regression
def test_RC002_obtener_comentario_id_mayuscula():
    """Test para verificar que se maneja un ID de comentario con letras mayúsculas."""
    thing_id = "N6N6I95"
    response = obtener_comentarios(thing_id)
    logging.info("Validando que se maneje un ID de comentario en mayuscula")
    assert_comentario_id_invalido(response)
    logging.info("El ID de comentario con mayuscula se maneja correctamente")



@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.ejecutar
def test_RC003_obtener_comentario_sin_token():
    """Test para verificar que no se permite obtener un comentario sin token de autenticación."""
    thing_id = "n6n6i95"
    response = obtener_comentario_token_sin_token(thing_id)
    logging.info("Validando que no se permite obtener un comentario sin token de autenticación")
    assert_comentario_sin_token(response)
    logging.info("No se permite obtener comentarios sin token de autenticación.")



@pytest.mark.functional
@pytest.mark.regression
def test_RC004_obtener_comentario_body_existe():
    """Test para verificar que el campo 'body' existe en la respuesta."""
    thing_id = "n6n6i95"  # Reemplaza con un ID de comentario válido
    response = obtener_comentarios(thing_id)
    logging.info("Validando que el campo 'body' exista en la respuesta")
    assert_existe_body(response)
    logging.info("El campo 'body' existe y no está vacío.")


@pytest.mark.functional
@pytest.mark.regression
def test_RC002_obtener_comentario_id_invalido():  # CAMBIAR EN ZEPHYR ID
    """Test para verificar que se maneja un ID de comentario inválido."""
    thing_id = "invalid_id"
    response = obtener_comentarios(thing_id)
    logging.info("Validando que se maneje un ID de comentario invalido")
    assert_comentario_id_invalido(response)




@pytest.mark.functional
@pytest.mark.regression
def test_RC004_obtener_comentario_body_existe():
    """Test para verificar que el campo 'body' existe en la respuesta."""
    thing_id = "n6n6i95"  
    response = obtener_comentarios(thing_id)
    logging.info("Validando que el campo 'body' exista en la respuesta")
    assert_existe_body(response)
    logging.info("El campo 'body' existe y no está vacío.")

# FALTA EL 006 007 008


