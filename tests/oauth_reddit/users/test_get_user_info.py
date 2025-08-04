import json
import requests
import pytest
import sys
import os
from dotenv import load_dotenv
import jsonschema  
from src.redditApi.get_user_info_api import obtener_informacion
from src.redditApi.get_user_info_api import obtener_informacion_con_token_caducado
from src.redditApi.get_user_info_api import obtener_informacion_con_token_invalido
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
    try:
        jsonschema.validate(instance=datos_entrada, schema=schema_user_input)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide {err}")

    respuesta = obtener_informacion(nombre_usuario)
    assert respuesta.status_code == 200
    
    try:
        jsonschema.validate(instance=respuesta.json(), schema=schema_user_info_exitosamente_respuesta)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide {err}")

@pytest.mark.functional   
@pytest.mark.regression 
def test_OI_003_obtener_info_usuario_inexistente():

    datos_entrada = {}
    nombre_usuario = "Ok-Low-25"
    try:
        jsonschema.validate(instance=datos_entrada, schema=schema_user_input)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide {err}")

    respuesta = obtener_informacion(nombre_usuario)
    assert respuesta.status_code == 404
    
    try:
        jsonschema.validate(instance=respuesta.json(), schema=schema_user_inexistente)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide {err}")

    
@pytest.mark.functional   
@pytest.mark.regression 
def test_OI_004_obtener_info_usuario_con_caracteres_especiales():

    datos_entrada = {}
    nombre_usuario = "Ok***/*/*"
    try:
        jsonschema.validate(instance=datos_entrada, schema=schema_user_input)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide {err}")

    respuesta = obtener_informacion(nombre_usuario)
    assert respuesta.status_code == 400
    
    try:
        jsonschema.validate(instance=respuesta.json(), schema=schema_user_inexistente)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide {err}")

@pytest.mark.functional  
@pytest.mark.regression  
def test_OI_005_obtener_info_token_caducado():

    datos_entrada = {}
    nombre_usuario = "Ok-Low-2580"
    try:
        jsonschema.validate(instance=datos_entrada, schema=schema_user_input)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide {err}")

    respuesta = obtener_informacion_con_token_caducado(nombre_usuario)
    assert respuesta.status_code == 401
    
@pytest.mark.functional 
@pytest.mark.regression   
def test_OI_006_obtener_info_token_invalido():

    datos_entrada = {}
    nombre_usuario = "Ok-Low-2580"
    try:
        jsonschema.validate(instance=datos_entrada, schema=schema_user_input)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide {err}")

    respuesta = obtener_informacion_con_token_invalido(nombre_usuario)
    assert respuesta.status_code == 403
    
@pytest.mark.functional 
@pytest.mark.regression   
def test_OI_007_obtener_info_usuario_propio():

    datos_entrada = {}
    nombre_usuario = os.getenv('REDDIT_USERNAME')
    try:
        jsonschema.validate(instance=datos_entrada, schema=schema_user_input)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide {err}")

    respuesta = obtener_informacion(nombre_usuario)
    assert respuesta.status_code == 200

    try:
        jsonschema.validate(instance=respuesta.json(), schema=schema_user_input_propio)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide {err}")
