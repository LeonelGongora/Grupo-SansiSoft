import requests
import pytest
import os
import time
from src.logs.logger import logger
from src.assertions.amigo_assertions import (
    assert_add_friend_successfully,
    assert_add_friend_success_response_schema,
    assert_add_friend_success_payload_schema
)
username_valid = "Spiritual-Pay-8530"
url = "https://oauth.reddit.com"
def getSubmitUrl(username):
    return f"{url}/api/v1/me/friends/{username}"
#Agregar amigo con nombre de usuario valido
@pytest.mark.smoke
@pytest.mark.functional
def test_AA001_add_friend_with_username_valid(get_token_fixture):
    """AA001 - Add a friend successfully"""
    headers = {
        "Authorization": f"Bearer {get_token_fixture}",
        "User-Agent": "SansiSofRFV/0.1 by IceOld4091",
        "Content-Type": "application/json",
    }
    payload = {"name": f"{username_valid}"}
    submit_url = f"{url}/api/v1/me/friends/{username_valid}"
    logger.debug("PUT " + submit_url+ " HEADERS" + str(headers))
    logger.debug("Payload: " + str(payload))
    assert_add_friend_success_payload_schema(payload)
    response = requests.put(submit_url, headers=headers, json=payload)

    logger.info("Status Code: " + str(response.status_code))
    logger.debug("Response: " + str(response.json()))
    # Assertions
    assert_add_friend_successfully(response)
    assert_add_friend_success_response_schema(response.json())
# Agregar amigo con nombre que ya es nuestro amigo
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.xfail(reason="El API permite agregar al mismo amigo dos veces, debería fallar")
def test_AA002_add_friend_existing(get_token_fixture):
    """AA001 - Debe fallar al agregar un amigo ya existente"""
    headers = {
        "Authorization": f"Bearer {get_token_fixture}",
        "User-Agent": "SansiSofRFV/0.1 by IceOld4091",
        "Content-Type": "application/json",
    }
    payload = {"name": f"{username_valid}"}
    submit_url = f"{url}/api/v1/me/friends/{username_valid}"
    assert_add_friend_success_payload_schema(payload)
    logger.debug("PUT " + submit_url+ " HEADERS" + str(headers))
    logger.debug("Payload: " + str(payload))
    response = requests.put(submit_url, headers=headers, json=payload)
    logger.info("Status Code: " + str(response.status_code))
    logger.debug("Response: " + str(response.json()))
    assert response.status_code != 200, f"Expected failure, but got 200: {response.json()}"

# Agregar amigo con nombre que NO existe
@pytest.mark.smoke
@pytest.mark.functional
def test_AA003_add_friend_nonexistent_user(get_token_fixture):
    """AA002 - Debe fallar al agregar un usuario de Reddit no existente"""
    username_invalid = "username_invalid"
    headers = {
        "Authorization": f"Bearer {get_token_fixture}",
        "User-Agent": "SansiSofRFV/0.1 by IceOld4091",
        "Content-Type": "application/json",
    }

    payload = {"name": username_invalid}
    submit_url = f"{url}/api/v1/me/friends/{username_invalid}"
    logger.debug("PUT " + submit_url+ " HEADERS" + str(headers))
    logger.debug("Payload: " + str(payload))
    assert_add_friend_success_payload_schema(payload)
    response = requests.put(submit_url, headers=headers, json=payload)
    logger.info("Status Code: " + str(response.status_code))
    logger.debug("Response: " + str(response.json()))
    if response.status_code != 404:
        pytest.xfail(f"Codigo esperado era 404, pero obtuvo {response.status_code}")
    
    assert response.status_code == 404
# Agregar amigo sin token → debe retornar 403
@pytest.mark.smoke
@pytest.mark.functional
def test_AA004_add_friend_without_token():
    """AA007 - Debe retornar 403 cuando no se envía access token"""
    headers = {
        "User-Agent": "SansiSofRFV/0.1 by IceOld4091",
        "Content-Type": "application/json",
    }
    payload = {"name": username_valid}
    submit_url = f"{url}/api/v1/me/friends/{username_valid}"
    assert_add_friend_success_payload_schema(payload)
    logger.debug("PUT " + submit_url+ " HEADERS" + str(headers))
    logger.debug("Payload: " + str(payload))
    response = requests.put(submit_url, headers=headers, json=payload)
    logger.info("Status Code: " + str(response.status_code))
    logger.debug("Response: " + str(response.text))
    if response.status_code != 403:
        pytest.xfail(f"Se esperaba el código 403 (Prohibido), pero se obtuvo {response.status_code}")
    
    assert response.status_code == 403

# Agregar amigo con token caducado → debe retornar 401
@pytest.mark.security
@pytest.mark.functional
def test_AA005_add_friend_with_expired_token():
    """AA005 - Debe retornar 401 cuando se usa un access token caducado"""
    expired_token = "Bearer expired_token_example"  # 👈 reemplaza por un token realmente caducado
    
    headers = {
        "Authorization": os.getenv("REDDIT_ACCESS_TOKEN_CADUCADO"),
        "User-Agent": "SansiSofRFV/0.1 by IceOld4091",
        "Content-Type": "application/json",
    }
    payload = {"name": username_valid}
    submit_url = f"{url}/api/v1/me/friends/{username_valid}"
    
    assert_add_friend_success_payload_schema(payload)
    
    logger.debug("PUT " + submit_url + " HEADERS " + str(headers))
    logger.debug("Payload: " + str(payload))
    
    response = requests.put(submit_url, headers=headers, json=payload)
    
    logger.info("Status Code: " + str(response.status_code))
    logger.debug("Response: " + str(response.text))

    if response.status_code != 401:
        pytest.xfail(f"Se esperaba el código 401 (No autorizado), pero se obtuvo {response.status_code}")

    assert response.status_code == 401

# Agregar amigo con token inválido → debe retornar 403
@pytest.mark.smoke
@pytest.mark.functional
def test_AA006_add_friend_with_invalid_token():
    """AA003 - Debe retornar 403 cuando se utiliza un token de acceso inválido"""
    invalid_token = "Bearer invalid_token_value"

    headers = {
        "Authorization": invalid_token,
        "User-Agent": "SansiSofRFV/0.1 by IceOld4091",
        "Content-Type": "application/json",
    }
    payload = {"name": username_valid}
    submit_url = f"{url}/api/v1/me/friends/{username_valid}"
    logger.debug("PUT " + submit_url+ " HEADERS" + str(headers))
    logger.debug("Payload: " + str(payload))
    assert_add_friend_success_payload_schema(payload)
    response = requests.put(submit_url, headers=headers, json=payload)
    logger.info("Status Code: " + str(response.status_code))
    logger.debug("Response: " + str(response.text))
    if response.status_code != 403:
        pytest.fail(f"Se esperaba el código 403 (Prohibido), pero se obtuvo {response.status_code}")
    else :
        assert response.status_code == 403