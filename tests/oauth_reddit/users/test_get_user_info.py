import json
import requests
import pytest
import sys
import os
from dotenv import load_dotenv
import jsonschema
from src.redditApi.get_user_info_api import obtener_informacion_exitosamente
from src.schemas.get_user_info.get_user_info_exitosamente_schema import schema_user_info_exitosamente
from src.schemas.get_user_info.get_user_info_exitosamente_response_schema import schema_user_info_exitosamente_respuesta

load_dotenv()

@pytest.mark.smoke
@pytest.mark.functional
def test_OI_001_obtener_info_usuario_existente():

    datos_entrada = {}
    parametro = "Ok-Low-2580"
    try:
        jsonschema.validate(instance=datos_entrada, schema=schema_user_info_exitosamente)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide {err}")

    respuesta = obtener_informacion_exitosamente(parametro)
    assert respuesta.status_code == 200
    
    try:
        jsonschema.validate(instance=respuesta.json(), schema=schema_user_info_exitosamente_respuesta)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"Esquema no coincide {err}")


    