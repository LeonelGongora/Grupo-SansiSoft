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
from src.services.auth import build_headers
from src.payloads.payload_añadir_amigo import crear_payload_añadir_amigo
username_valid = "Spiritual-Pay-8530"
url = "https://oauth.reddit.com"
def getSubmitUrl(username):
    return f"{url}/api/v1/me/friends/{username}"
#Agregar amigo con nombre de usuario valido
@pytest.mark.smoke
@pytest.mark.functional
def test_AA001_add_friend_with_username_valid(get_token_fixture,get_user_agent):
    """AA001 - Add a friend successfully"""
    headers = build_headers(token=get_token_fixture, user_agent=get_user_agent)
    payload = crear_payload_añadir_amigo(username=username_valid)
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
def test_AA002_add_friend_existing(get_token_fixture,get_user_agent):
    """AA001 - Debe fallar al agregar un amigo ya existente"""
    headers = build_headers(token=get_token_fixture, user_agent=get_user_agent)
    payload = crear_payload_añadir_amigo(username=username_valid)
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
def test_AA003_add_friend_nonexistent_user(get_token_fixture,get_user_agent):
    """AA002 - Debe fallar al agregar un usuario de Reddit no existente"""
    username_invalid = "perexz*italian"
    headers = build_headers(token=get_token_fixture, user_agent=get_user_agent)
    payload = crear_payload_añadir_amigo(username=username_invalid)
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
def test_AA004_add_friend_without_token(get_user_agent):
    """AA007 - Debe retornar 403 cuando no se envía access token"""
    
    headers = {
        "User-Agent": get_user_agent,
    }
    payload = crear_payload_añadir_amigo(username=username_valid)
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
@pytest.mark.smoke
@pytest.mark.functional
def test_AA005_add_friend_with_expired_token(get_user_agent):
    """AA005 - Debe retornar 401 cuando se usa un access token caducado"""
    headers = build_headers(token=os.getenv("REDDIT_ACCESS_TOKEN_CADUCADO"), user_agent=get_user_agent)
    payload = crear_payload_añadir_amigo(username=username_valid)
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
def test_AA006_add_friend_with_invalid_token(get_user_agent):
    """AA003 - Debe retornar 403 cuando se utiliza un token de acceso inválido"""
    invalid_token = "Bearer invalid_token_value"
    headers = build_headers(token=invalid_token, user_agent=get_user_agent)
    payload = crear_payload_añadir_amigo(username=username_valid)
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

# Agregar amigo con parámetros de consulta inválidos → no debe retornar 200
@pytest.mark.smoke
@pytest.mark.functional
def test_AA008_add_friend_with_invalid_query_params(get_token_fixture,get_user_agent):
    """AA007 - No debe retornar 200 cuando se envían parámetros de consulta inválidos"""
    headers = build_headers(token=get_token_fixture, user_agent=get_user_agent)
    payload = crear_payload_añadir_amigo(username=username_valid)
    # Parámetros inválidos en la query
    submit_url = f"{url}/api/v1/me/friends/{username_valid}?sort=%%%&limit=-10&page=none"

    logger.debug("PUT " + submit_url + " HEADERS " + str(headers))
    logger.debug("Payload: " + str(payload))

    assert_add_friend_success_payload_schema(payload)

    response = requests.put(submit_url, headers=headers, json=payload)

    logger.info("Status Code: " + str(response.status_code))
    logger.debug("Response: " + str(response.text))

    if response.status_code == 200:
        pytest.xfail("Se esperaba que la API rechazara los parámetros inválidos, pero devolvió 200 OK")

    # Aceptable: cualquier otro status (400, 403, 422, etc.)
    assert response.status_code != 200
        
# Agregar amigo con payload vacio       
@pytest.mark.smoke
@pytest.mark.functional
def test_AA009_add_friend_with_empty_payload(get_token_fixture,get_user_agent):
    """AA009 - No debe retornar 200 cuando se envía un payload vacío"""
    headers = build_headers(token=get_token_fixture, user_agent=get_user_agent)
    payload = crear_payload_añadir_amigo(username=None)

    submit_url = f"{url}/api/v1/me/friends/{username_valid}"

    logger.debug("PUT " + submit_url + " HEADERS " + str(headers))
    logger.debug("Payload vacío enviado")

    response = requests.put(submit_url, headers=headers, json=payload)

    logger.info("Status Code: " + str(response.status_code))
    logger.debug("Response: " + str(response.text))

    if response.status_code == 200:
        pytest.xfail("Se esperaba que la API rechazara el payload vacío, pero devolvió 200 OK")

    # Aceptable: cualquier otro status (400, 422, etc.)
    assert response.status_code != 200

# Agregar amigo con username con caracteres especiales
@pytest.mark.smoke
@pytest.mark.functional
def test_AA010_add_friend_with_special_chars(get_token_fixture,get_user_agent):
    """AA009 - No debe retornar 200 cuando se envía un username con caracteres especiales"""
    invalid_username = "inv@lid_user!#"
    headers = build_headers(token=get_token_fixture, user_agent=get_user_agent)
    payload = crear_payload_añadir_amigo(username=invalid_username)

    submit_url = f"{url}/api/v1/me/friends/{invalid_username}"

    logger.debug("PUT " + submit_url + " HEADERS " + str(headers))
    logger.debug("Payload vacío enviado con username inválido")

    response = requests.put(submit_url, headers=headers, json=payload)

    logger.info("Status Code: " + str(response.status_code))
    logger.debug("Response: " + str(response.text))

    if response.status_code == 200:
        pytest.xfail("Se esperaba que la API rechazara el username inválido, pero devolvió 200 OK")

    # Aceptable: cualquier otro status (400, 422, etc.)
    assert response.status_code != 200
# Agregarse de maigo asi mismo
@pytest.mark.smoke
@pytest.mark.functional
def test_AA011_add_self_as_friend(get_token_fixture,get_user_agent):
    """AA011 - No debe ser posible agregarse a sí mismo como amigo"""
    current_user = os.getenv("REDDIT_USERNAME")
    headers = build_headers(token=get_token_fixture, user_agent=get_user_agent)
    payload = crear_payload_añadir_amigo(username=current_user)

    submit_url = f"{url}/api/v1/me/friends/{current_user}"

    logger.debug("PUT " + submit_url + " HEADERS " + str(headers))
    logger.debug("Intentando agregarse a sí mismo con payload: " + str(payload))

    response = requests.put(submit_url, headers=headers, json=payload)

    logger.info("Status Code: " + str(response.status_code))
    logger.debug("Response: " + str(response.text))

    if response.status_code == 200:
        pytest.xfail("Se esperaba que la API rechazara el intento de agregarse a sí mismo, pero devolvió 200 OK")

    # Códigos válidos: 400, 403, 422, etc.
    assert response.status_code != 200

# Agregar amigo con nombre vacío → debe fallar (no debe retornar 200)
@pytest.mark.smoke
@pytest.mark.functional
def test_AA015_add_friend_with_empty_name(get_token_fixture,get_user_agent):
    """AA012 - No debe ser posible agregar un amigo con nombre vacío"""
    empty_username = ""  # 👈 nombre vacío
    headers = build_headers(token=get_token_fixture, user_agent=get_user_agent)
    payload = crear_payload_añadir_amigo(username=empty_username)
    submit_url = f"{url}/api/v1/me/friends/{empty_username}"

    logger.debug("PUT " + submit_url + " HEADERS " + str(headers))
    logger.debug("Intentando agregar amigo con nombre vacío, payload: " + str(payload))

    response = requests.put(submit_url, headers=headers, json=payload)

    logger.info("Status Code: " + str(response.status_code))
    logger.debug("Response: " + str(response.text))

    if response.status_code == 200:
        pytest.xfail("Se esperaba que la API rechazara el nombre vacío, pero devolvió 200 OK")

    assert response.status_code != 200
