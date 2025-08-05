import json
import requests
import pytest
import sys
import os
from dotenv import load_dotenv
from src.logs.logger import logger 
import jsonschema 
from src.redditApi.post_report_user_api import reportar_usuario_exitosamente
from src.redditApi.post_report_user_api import reportar_usuario_con_token_invalido
from src.redditApi.post_report_user_api import reportar_usuario_sin_token
from src.redditApi.post_report_user_api import reportar_usuario_token_vencido  
from src.redditApi.post_report_user_api import reportar_usuario_sin_reason
from src.schemas.report_user.post_report_user_exitosamente_input_schema import schema_report_user_input
from src.schemas.report_user.post_report_user_exitosamente_response_schema import schema_report_user_respuesta_exitosa
from src.schemas.report_user.post_report_user_sin_token_response_schema import schema_report_user_sin_token 
from src.schemas.report_user.post_report_user_sin_reason_schema import schema_report_user_sin_razon

load_dotenv()

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression 
def test_OI_001_reportar_usuario_exitosamente():
    logger.info("Iniciando test_OI_001_reportar_usuario_exitosamente")
    datos_entrada = {
        "user": "Ok-Low-2580",
        "reason": "Este es un motivo para reportar a un usuario"
    }
    logger.info(f"Datos de entrada: {datos_entrada}")
    try:
        jsonschema.validate(instance=datos_entrada, schema=schema_report_user_input)
        logger.info("Esquema de entrada validado correctamente")
    except jsonschema.exceptions.ValidationError as err:
        logger.error(f"Error en esquema de entrada: {err}")
        pytest.fail(f"Esquema no coincide {err}")
    
    respuesta = reportar_usuario_exitosamente(datos_entrada["user"], datos_entrada["reason"])
    logger.info(f"Respuesta HTTP: status_code={respuesta.status_code}")
    logger.debug(f"Cuerpo de respuesta: {respuesta.text}")
    assert respuesta.status_code == 200

    try:
        jsonschema.validate(instance=respuesta.json(), schema=schema_report_user_respuesta_exitosa)
        logger.info("Esquema de salida validado correctamente")
    except jsonschema.exceptions.ValidationError as err:
        logger.error(f"Error en esquema de salida: {err}")
        pytest.fail(f"Esquema no coincide {err}")

@pytest.mark.functional
@pytest.mark.regression 
@pytest.mark.xfail(reason="BUG-001-USER003: Se obtiene un codigo 200 cuando se envia un usuario inexistente en el payload")
def test_REPU_002_reportar_usuario_inexistente():
    logger.info("Iniciando test_REPU_002_reportar_usuario_inexistente")
    datos_entrada = {
        "user": "Ok-Low-25",
        "reason": "Este es un motivo para reportar a un usuario"
    }
    logger.info(f"Datos de entrada: {datos_entrada}")
    try:    
        jsonschema.validate(instance=datos_entrada, schema=schema_report_user_input)
        logger.info("Esquema de entrada validado correctamente")
    except jsonschema.exceptions.ValidationError as err:
        logger.error(f"Error en esquema de entrada: {err}")
        pytest.fail(f"Esquema no coincide {err}")
    
    respuesta = reportar_usuario_exitosamente(datos_entrada["user"], datos_entrada["reason"])
    logger.info(f"Respuesta HTTP: status_code={respuesta.status_code}")
    logger.debug(f"Cuerpo de respuesta: {respuesta.text}")
    assert respuesta.status_code == 404

    try:
        jsonschema.validate(instance=respuesta.json(), schema=schema_report_user_respuesta_exitosa)
        logger.info("Esquema de salida validado correctamente")
    except jsonschema.exceptions.ValidationError as err:
        logger.error(f"Error en esquema de salida: {err}")
        pytest.fail(f"Esquema no coincide {err}")

@pytest.mark.functional
@pytest.mark.regression 
def test_REPU_003_reportar_usuario_con_token_invalido():
    logger.info("Iniciando test_REPU_003_reportar_usuario_con_token_invalido")
    datos_entrada = {
        "user": "Ok-Low-2580",
        "reason": "Este es un motivo para reportar a un usuario"
    }
    logger.info(f"Datos de entrada: {datos_entrada}")
    try:
        jsonschema.validate(instance=datos_entrada, schema=schema_report_user_input)
        logger.info("Esquema de entrada validado correctamente")
    except jsonschema.exceptions.ValidationError as err:
        logger.error(f"Error en esquema de entrada: {err}")
        pytest.fail(f"Esquema no coincide {err}")
    
    respuesta = reportar_usuario_con_token_invalido(datos_entrada["user"], datos_entrada["reason"])
    logger.info(f"Respuesta HTTP: status_code={respuesta.status_code}")
    assert respuesta.status_code == 403

@pytest.mark.functional
def test_REPU_004_reportar_usuario_sin_token():
    logger.info("Iniciando test_REPU_004_reportar_usuario_sin_token")
    datos_entrada = {
        "user": "Ok-Low-2580",
        "reason": "Este es un motivo para reportar a un usuario"
    }
    logger.info(f"Datos de entrada: {datos_entrada}")
    try:
        jsonschema.validate(instance=datos_entrada, schema=schema_report_user_input)
        logger.info("Esquema de entrada validado correctamente")
    except jsonschema.exceptions.ValidationError as err:
        logger.error(f"Error en esquema de entrada: {err}")
        pytest.fail(f"Esquema no coincide {err}")
    
    respuesta = reportar_usuario_sin_token(datos_entrada["user"], datos_entrada["reason"])
    logger.info(f"Respuesta HTTP: status_code={respuesta.status_code}")
    logger.debug(f"Cuerpo de respuesta: {respuesta.text}")
    assert respuesta.status_code == 200

    try:
        jsonschema.validate(instance=respuesta.json(), schema=schema_report_user_sin_token)
        logger.info("Esquema de salida validado correctamente")
    except jsonschema.exceptions.ValidationError as err:
        logger.error(f"Error en esquema de salida: {err}")
        pytest.fail(f"Esquema no coincide {err}")

@pytest.mark.functional
def test_REPU_005_reportar_usuario_token_vencido():
    logger.info("Iniciando test_REPU_005_reportar_usuario_token_vencido")
    datos_entrada = {
        "user": "Ok-Low-2580",
        "reason": "Este es un motivo para reportar a un usuario"
    }
    logger.info(f"Datos de entrada: {datos_entrada}")
    try:
        jsonschema.validate(instance=datos_entrada, schema=schema_report_user_input)
        logger.info("Esquema de entrada validado correctamente")
    except jsonschema.exceptions.ValidationError as err:
        logger.error(f"Error en esquema de entrada: {err}")
        pytest.fail(f"Esquema no coincide {err}")
    
    respuesta = reportar_usuario_token_vencido(datos_entrada["user"], datos_entrada["reason"])
    logger.info(f"Respuesta HTTP: status_code={respuesta.status_code}")
    assert respuesta.status_code == 401

@pytest.mark.functional
@pytest.mark.regression 
@pytest.mark.xfail(reason="BUG-002-USER003: Se obtiene un codigo 200 cuando se envia un reason de mas de 100 caracteres en el payload")
def test_REPU_006_reportar_usuario_con_reason_superando_100_caracteres():
    logger.info("Iniciando test_REPU_006_reportar_usuario_con_reason_superando_100_caracteres")
    datos_entrada = {
        "user": "Ok-Low-2580",
        "reason": "Este es un motivo de reporte que excede el límite permitido de cien caracteres, y por tanto debería fallar."
    }
    logger.info(f"Datos de entrada: {datos_entrada}")
    try:
        jsonschema.validate(instance=datos_entrada, schema=schema_report_user_input)
        logger.info("Esquema de entrada validado correctamente")
    except jsonschema.exceptions.ValidationError as err:
        logger.error(f"Error en esquema de entrada: {err}")
        pytest.fail(f"Esquema no coincide {err}")
    
    respuesta = reportar_usuario_exitosamente(datos_entrada["user"], datos_entrada["reason"])
    logger.info(f"Respuesta HTTP: status_code={respuesta.status_code}")
    logger.debug(f"Cuerpo de respuesta: {respuesta.text}")
    assert respuesta.status_code == 400

@pytest.mark.functional
@pytest.mark.regression 
@pytest.mark.xfail(reason="BUG-003-USER003: Se obtiene un código 200 cuando se reporta a un nombre de usuario con caracteres especiales.")
def test_REPU_007_reportar_usuario_con_carateres_especiales():
    logger.info("Iniciando test_REPU_007_reportar_usuario_con_carateres_especiales")
    datos_entrada = {
        "user": "Ok***/*/*",
        "reason": "Este es un motivo para reportar a un usuario"
    }
    logger.info(f"Datos de entrada: {datos_entrada}")
    try:
        jsonschema.validate(instance=datos_entrada, schema=schema_report_user_input)
        logger.info("Esquema de entrada validado correctamente")
    except jsonschema.exceptions.ValidationError as err:
        logger.error(f"Error en esquema de entrada: {err}")
        pytest.fail(f"Esquema no coincide {err}")
    
    respuesta = reportar_usuario_exitosamente(datos_entrada["user"], datos_entrada["reason"])
    logger.info(f"Respuesta HTTP: status_code={respuesta.status_code}")
    logger.debug(f"Cuerpo de respuesta: {respuesta.text}")
    assert respuesta.status_code == 400
    
@pytest.mark.functional
@pytest.mark.regression 
@pytest.mark.xfail(reason="BUG-004-USER003: Se obtiene un codigo 200 cuando se envia una solicitud con usuario vacio")
def test_REPU_008_reportar_usuario_con_nombre_usuario_vacio():
    logger.info("Iniciando test_REPU_008_reportar_usuario_con_nombre_usuario_vacio")
    datos_entrada = {
        "user": "",
        "reason": "Este es un motivo para reportar a un usuario"
    }
    logger.info(f"Datos de entrada: {datos_entrada}")
    try:
        jsonschema.validate(instance=datos_entrada, schema=schema_report_user_input)
        logger.info("Esquema de entrada validado correctamente")
    except jsonschema.exceptions.ValidationError as err:
        logger.error(f"Error en esquema de entrada: {err}")
        pytest.fail(f"Esquema no coincide {err}")
    
    respuesta = reportar_usuario_exitosamente(datos_entrada["user"], datos_entrada["reason"])
    logger.info(f"Respuesta HTTP: status_code={respuesta.status_code}")
    logger.debug(f"Cuerpo de respuesta: {respuesta.text}")
    assert respuesta.status_code == 400
    
@pytest.mark.functional
@pytest.mark.regression 
@pytest.mark.xfail(reason="BUG-005-USER003: Se obtiene un código 200 cuando se reporta al nombre de usuario propio")
def test_REPU_009_reportar_nombre_usuario_propio():
    logger.info("Iniciando test_REPU_009_reportar_nombre_usuario_propio")
    datos_entrada = {
        "user": os.getenv('REDDIT_USERNAME'),
        "reason": "Este es un motivo para reportar a un usuario"
    }
    logger.info(f"Datos de entrada: {datos_entrada}")
    try:
        jsonschema.validate(instance=datos_entrada, schema=schema_report_user_input)
        logger.info("Esquema de entrada validado correctamente")
    except jsonschema.exceptions.ValidationError as err:
        logger.error(f"Error en esquema de entrada: {err}")
        pytest.fail(f"Esquema no coincide {err}")
    
    respuesta = reportar_usuario_exitosamente(datos_entrada["user"], datos_entrada["reason"])
    logger.info(f"Respuesta HTTP: status_code={respuesta.status_code}")
    logger.debug(f"Cuerpo de respuesta: {respuesta.text}")
    assert respuesta.status_code == 400

@pytest.mark.functional
@pytest.mark.regression 
@pytest.mark.xfail(reason="BUG-006-USER003: Se obtiene un codigo 200 cuando se reporta a un usuario sin el campo reason en el body")
def test_REPU_010_reportar_usuario_sin_reason():
    logger.info("Iniciando test_REPU_010_reportar_usuario_sin_reason")
    datos_entrada = {
        "user": "Ok-Low-2580",
    }
    logger.info(f"Datos de entrada: {datos_entrada}")
    try:
        jsonschema.validate(instance=datos_entrada, schema=schema_report_user_sin_razon)
        logger.info("Esquema de entrada validado correctamente")
    except jsonschema.exceptions.ValidationError as err:
        logger.error(f"Error en esquema de entrada: {err}")
        pytest.fail(f"Esquema no coincide {err}")
    
    respuesta = reportar_usuario_sin_reason(datos_entrada["user"])
    logger.info(f"Respuesta HTTP: status_code={respuesta.status_code}")
    logger.debug(f"Cuerpo de respuesta: {respuesta.text}")
    assert respuesta.status_code == 400