import json
import requests
import pytest
import sys
import os
from dotenv import load_dotenv
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
def test_OI_001_reportar_usuario_exitosamentea():

    datos_entrada = {
        "user": os.getenv('REDDIT_USERNAME_VALIDO'),
        "reason": "Este es un motivo para reportar a un usuario"
    }

    try:
        jsonschema.validate(instance=datos_entrada, schema=schema_report_user_input)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide {err}")
    
    respuesta = reportar_usuario_exitosamente(datos_entrada["user"], datos_entrada["reason"])
    assert respuesta.status_code == 200

    try:
        jsonschema.validate(instance=respuesta.json(), schema=schema_report_user_respuesta_exitosa)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide {err}")

@pytest.mark.functional
@pytest.mark.regression 
def test_REPU_002_reportar_usuario_inexistente():

    datos_entrada = {
        "user": os.getenv('REDDIT_USERNAME_INEXISTENTE'),
        "reason": "Este es un motivo para reportar a un usuario"
    }

    try:
        jsonschema.validate(instance=datos_entrada, schema=schema_report_user_input)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide {err}")
    
    respuesta = reportar_usuario_exitosamente(datos_entrada["user"], datos_entrada["reason"])
    assert respuesta.status_code == 404

    try:
        jsonschema.validate(instance=respuesta.json(), schema=schema_report_user_respuesta_exitosa)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide {err}")

@pytest.mark.functional
@pytest.mark.regression 
def test_REPU_003_reportar_usuario_con_token_invalido():

    datos_entrada = {
        "user": os.getenv('REDDIT_USERNAME_VALIDO'),
        "reason": "Este es un motivo para reportar a un usuario"
    }

    try:
        jsonschema.validate(instance=datos_entrada, schema=schema_report_user_input)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide {err}")
    
    respuesta = reportar_usuario_con_token_invalido(datos_entrada["user"], datos_entrada["reason"])
    assert respuesta.status_code == 403

@pytest.mark.functional
@pytest.mark.regression 
def test_REPU_004_reportar_usuario_sin_token():

    datos_entrada = {
        "user": os.getenv('REDDIT_USERNAME_VALIDO'),
        "reason": "Este es un motivo para reportar a un usuario"
    }

    try:
        jsonschema.validate(instance=datos_entrada, schema=schema_report_user_input)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide {err}")
    
    respuesta = reportar_usuario_sin_token(datos_entrada["user"], datos_entrada["reason"])
    assert respuesta.status_code == 200

    try:
        jsonschema.validate(instance=respuesta.json(), schema=schema_report_user_sin_token)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide {err}")

@pytest.mark.functional
@pytest.mark.regression 
def test_OI_005_reportar_usuario_token_vencido():

    datos_entrada = {
        "user": os.getenv('REDDIT_USERNAME_VALIDO'),
        "reason": "Este es un motivo para reportar a un usuario"
    }

    try:
        jsonschema.validate(instance=datos_entrada, schema=schema_report_user_input)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide {err}")
    
    respuesta = reportar_usuario_token_vencido(datos_entrada["user"], datos_entrada["reason"])
    assert respuesta.status_code == 401

@pytest.mark.functional
@pytest.mark.regression 
def test_OI_006_reportar_usuario_con_reason_superando_100_caracteres():

    datos_entrada = {
        "user": os.getenv('REDDIT_USERNAME_VALIDO'),
        "reason": os.getenv('REDDIT_RAZON_MAS_100_CARACTERES')
    }

    try:
        jsonschema.validate(instance=datos_entrada, schema=schema_report_user_input)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide {err}")
    
    respuesta = reportar_usuario_exitosamente(datos_entrada["user"], datos_entrada["reason"])
    assert respuesta.status_code == 400

@pytest.mark.functional
@pytest.mark.regression 
def test_OI_007_reportar_usuario_con_carateres_especiales():

    datos_entrada = {
        "user": os.getenv('REDDIT_USERNAME_CARACTERES_ESPECIALES'),
        "reason": "Este es un motivo para reportar a un usuario"
    }

    try:
        jsonschema.validate(instance=datos_entrada, schema=schema_report_user_input)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide {err}")
    
    respuesta = reportar_usuario_exitosamente(datos_entrada["user"], datos_entrada["reason"])
    assert respuesta.status_code == 400
    
@pytest.mark.functional
@pytest.mark.regression 
def test_OI_008_reportar_usuario_con_nombre_usuario_vacio():

    datos_entrada = {
        "user": "",
        "reason": "Este es un motivo para reportar a un usuario"
    }

    try:
        jsonschema.validate(instance=datos_entrada, schema=schema_report_user_input)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide {err}")
    
    respuesta = reportar_usuario_exitosamente(datos_entrada["user"], datos_entrada["reason"])
    assert respuesta.status_code == 400
    
@pytest.mark.functional
@pytest.mark.regression 
def test_OI_009_reportar_nombre_usuario_propio():

    datos_entrada = {
        "user": os.getenv('REDDIT_USERNAME'),
        "reason": "Este es un motivo para reportar a un usuario"
    }

    try:
        jsonschema.validate(instance=datos_entrada, schema=schema_report_user_input)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide {err}")
    
    respuesta = reportar_usuario_exitosamente(datos_entrada["user"], datos_entrada["reason"])
    assert respuesta.status_code == 400

@pytest.mark.functional
@pytest.mark.regression 
def test_OI_010_reportar_usuario_sin_reason():

    datos_entrada = {
        "user": os.getenv('REDDIT_USERNAME_VALIDO'),
    }

    try:
        jsonschema.validate(instance=datos_entrada, schema=schema_report_user_sin_razon)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide {err}")
    
    respuesta = reportar_usuario_sin_reason(datos_entrada["user"])
    assert respuesta.status_code == 400