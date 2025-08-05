import json
import requests
import pytest
import sys
import os
import logging
from dotenv import load_dotenv
from src.logs.logger import logger 
import jsonschema  
from src.redditApi.get_user_info_api import obtener_informacion
from src.redditApi.get_user_info_api import obtener_informacion_con_token_caducado
from src.redditApi.get_user_info_api import obtener_informacion_con_token_invalido 
from src.redditApi.get_user_info_api import obtener_informacion_con_usuario_vacio 
from src.redditApi.get_user_info_api import obtener_informacion_sin_token 
from src.schemas.get_user_info.get_user_info_exitosamente_schema import schema_user_input
from src.schemas.get_user_info.get_user_info_exitosamente_response_schema import schema_user_info_exitosamente_respuesta
from src.schemas.get_user_info.get_user_info_usuario_inexistente_response_schema import schema_user_inexistente           
from src.schemas.get_user_info.get_user_info_propio_schema import schema_user_input_propio
load_dotenv()

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_OI_001_obtener_info_usuario_existente():

    datos_entrada = {}
    nombre_usuario = "Ok-Low-2580"
    logger.info("Iniciando test_OI_001_obtener_info_usuario_existente")
    logger.info(f"Nombre de usuario obtenido: {nombre_usuario}")
    try:
        logger.info("Esquema de entrada validado correctamente")
        jsonschema.validate(instance=datos_entrada, schema=schema_user_input)
    except jsonschema.exceptions.ValidationError as err:
        logger.error(f"Error de validación del esquema de entrada: {err}")
        pytest.fail(f"Esquema no coincide {err}")

    respuesta = obtener_informacion(nombre_usuario)
    logger.info(f"Respuesta HTTP recibida: status_code={respuesta.status_code}")
    logger.debug(f"Cuerpo de la respuesta: {respuesta.text}")
    assert respuesta.status_code == 200
    
    try:
        logger.info("Esquema de salida validado correctamente")
        jsonschema.validate(instance=respuesta.json(), schema=schema_user_info_exitosamente_respuesta)
    except jsonschema.exceptions.ValidationError as err:
        logger.error(f"Error de validación del esquema de salida: {err}")
        pytest.fail(f"Esquema no coincide {err}")

@pytest.mark.functional   
@pytest.mark.regression 
def test_OI_003_obtener_info_usuario_inexistente():

    datos_entrada = {}
    nombre_usuario = "Ok-Low-25"
    logger.info("Iniciando test_OI_003_obtener_info_usuario_inexistente")
    logger.info(f"Nombre de usuario obtenido: {nombre_usuario}")
    try:
        logger.info("Esquema de entrada validado correctamente")
        jsonschema.validate(instance=datos_entrada, schema=schema_user_input)
    except jsonschema.exceptions.ValidationError as err:
        logger.error(f"Error de validación del esquema de entrada: {err}")
        pytest.fail(f"Esquema no coincide {err}")

    respuesta = obtener_informacion(nombre_usuario)
    logger.info(f"Respuesta HTTP recibida: status_code={respuesta.status_code}")
    logger.debug(f"Cuerpo de la respuesta: {respuesta.text}")
    assert respuesta.status_code == 404
    
    try:
        logger.info("Esquema de salida validado correctamente")
        jsonschema.validate(instance=respuesta.json(), schema=schema_user_inexistente)
    except jsonschema.exceptions.ValidationError as err:
        logger.error(f"Error de validación del esquema de salida: {err}")
        pytest.fail(f"Esquema no coincide {err}")

    
@pytest.mark.functional   
@pytest.mark.regression 
def test_OI_004_obtener_info_usuario_con_caracteres_especiales():

    datos_entrada = {}
    nombre_usuario = "Ok***/*/*"
    logger.info("Iniciando test_OI_004_obtener_info_usuario_con_caracteres_especiales")
    logger.info(f"Nombre de usuario obtenido: {nombre_usuario}")
    try:
        logger.info("Esquema de entrada validado correctamente")
        jsonschema.validate(instance=datos_entrada, schema=schema_user_input)
    except jsonschema.exceptions.ValidationError as err:
        logger.error(f"Error de validación del esquema de entrada: {err}")
        pytest.fail(f"Esquema no coincide {err}")

    respuesta = obtener_informacion(nombre_usuario)
    logger.info(f"Respuesta HTTP recibida: status_code={respuesta.status_code}")
    logger.debug(f"Cuerpo de la respuesta: {respuesta.text}")
    assert respuesta.status_code == 400
    
    try:
        logging.info("Esquema de salida validado correctamente")
        jsonschema.validate(instance=respuesta.json(), schema=schema_user_inexistente)
    except jsonschema.exceptions.ValidationError as err:
        logging.error(f"Error de validación del esquema de salida: {err}")
        pytest.fail(f"Esquema no coincide {err}")

@pytest.mark.functional  
@pytest.mark.regression  
def test_OI_005_obtener_info_token_caducado():

    datos_entrada = {}
    nombre_usuario = "Ok-Low-2580"
    logger.info("Iniciando test_OI_005_obtener_info_token_caducado")
    logger.info(f"Nombre de usuario obtenido: {nombre_usuario}")
    try:
        logger.info("Esquema de entrada validado correctamente")
        jsonschema.validate(instance=datos_entrada, schema=schema_user_input)
    except jsonschema.exceptions.ValidationError as err:
        logger.error(f"Error de validación del esquema de entrada: {err}")
        pytest.fail(f"Esquema no coincide {err}")

    respuesta = obtener_informacion_con_token_caducado(nombre_usuario)
    logger.info(f"Respuesta HTTP recibida: status_code={respuesta.status_code}")
    logger.debug(f"Cuerpo de la respuesta: {respuesta.text}")
    assert respuesta.status_code == 401
    
@pytest.mark.functional 
@pytest.mark.regression   
def test_OI_006_obtener_info_token_invalido():

    datos_entrada = {}
    nombre_usuario = "Ok-Low-2580"
    logger.info("Iniciando test_OI_006_obtener_info_token_invalido")
    logger.info(f"Nombre de usuario obtenido: {nombre_usuario}")
    try:
        logger.info("Esquema de entrada validado correctamente")
        jsonschema.validate(instance=datos_entrada, schema=schema_user_input)
    except jsonschema.exceptions.ValidationError as err:
        logger.error(f"Error de validación del esquema de entrada: {err}")
        pytest.fail(f"Esquema no coincide {err}")

    respuesta = obtener_informacion_con_token_invalido(nombre_usuario)
    logger.info(f"Respuesta HTTP recibida: status_code={respuesta.status_code}")
    logger.debug(f"Cuerpo de la respuesta: {respuesta.text}")
    assert respuesta.status_code == 403
    
@pytest.mark.functional 
@pytest.mark.regression   
def test_OI_007_obtener_info_usuario_propio():

    datos_entrada = {}
    nombre_usuario = os.getenv('REDDIT_USERNAME')
    logger.info("Iniciando test_OI_007_obtener_info_usuario_propio")
    logger.info(f"Nombre de usuario obtenido: {nombre_usuario}")
    try:
        logger.info("Esquema de entrada validado correctamente")
        jsonschema.validate(instance=datos_entrada, schema=schema_user_input)
    except jsonschema.exceptions.ValidationError as err:
        logger.error(f"Error de validación del esquema de entrada: {err}")
        pytest.fail(f"Esquema no coincide {err}")

    respuesta = obtener_informacion(nombre_usuario)
    logger.info(f"Respuesta HTTP recibida: status_code={respuesta.status_code}")
    logger.debug(f"Cuerpo de la respuesta: {respuesta.text}")
    assert respuesta.status_code == 200

    try:
        logger.info("Esquema de salida validado correctamente")
        jsonschema.validate(instance=respuesta.json(), schema=schema_user_input_propio)
    except jsonschema.exceptions.ValidationError as err:
        logger.error(f"Error de validación del esquema de salida: {err}")
        pytest.fail(f"Esquema no coincide {err}")

@pytest.mark.functional 
@pytest.mark.regression   
@pytest.mark.xfail(reason="BUG-001-USER004: Se obtiene un código 200 cuando no se ingresa ningun nombre de usuario en el parámetro de la api")
def test_OI_008_obtener_info_usuario_vacio():

    datos_entrada = {}
    logger.info("Iniciando test_OI_008_obtener_info_usuario_vacio")
    logger.info(f"Nombre de usuario obtenido: ")
    try:
        logger.info("Esquema de entrada validado correctamente")
        jsonschema.validate(instance=datos_entrada, schema=schema_user_input)
    except jsonschema.exceptions.ValidationError as err:
        logger.error(f"Error de validación del esquema de entrada: {err}")
        pytest.fail(f"Esquema no coincide {err}")

    respuesta = obtener_informacion_con_usuario_vacio()
    logger.info(f"Respuesta HTTP recibida: status_code={respuesta.status_code}")
    logger.debug(f"Cuerpo de la respuesta: {respuesta.text}")
    assert respuesta.status_code == 404
    

    try:
        logging.info("Esquema de salida validado correctamente")
        jsonschema.validate(instance=respuesta.json(), schema=schema_user_inexistente)
    except jsonschema.exceptions.ValidationError as err:
        logging.error(f"Error de validación del esquema de salida: {err}")
        pytest.fail(f"Esquema no coincide {err}")

@pytest.mark.functional 
@pytest.mark.regression   
def test_OI_009_obtener_info_sin_cabecera_authorization():

    datos_entrada = {}
    nombre_usuario = "Ok-Low-2580"
    logger.info("Iniciando test_OI_007_obtener_info_usuario_propio")
    logger.info(f"Nombre de usuario obtenido: {nombre_usuario}")
    try:
        logger.info("Esquema de entrada validado correctamente")
        jsonschema.validate(instance=datos_entrada, schema=schema_user_input)
    except jsonschema.exceptions.ValidationError as err:
        logger.error(f"Error de validación del esquema de entrada: {err}")
        pytest.fail(f"Esquema no coincide {err}")

    respuesta = obtener_informacion_sin_token(nombre_usuario)
    logger.info(f"Respuesta HTTP recibida: status_code={respuesta.status_code}")
    logger.debug(f"Cuerpo de la respuesta: {respuesta.text}")
    assert respuesta.status_code == 404

    