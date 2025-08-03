import json
import requests
import pytest
import sys
import os
from dotenv import load_dotenv
import jsonschema
from src.redditApi.get_user_info_api import obtener_informacion
from src.schemas.get_user_info.get_user_info_exitosamente_schema import schema_user_input
from src.schemas.get_user_info.get_user_info_exitosamente_response_schema import schema_user_info_exitosamente_respuesta
from src.schemas.get_user_info.get_user_info_usuario_inexistente_response_schema import schema_user_inexistente          

load_dotenv()

@pytest.mark.smoke
@pytest.mark.functional
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

    