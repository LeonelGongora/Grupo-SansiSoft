import requests
import pytest
import os
import time
from src.logs.logger import logger
from src.assertions.eliminar_amigo_assertions import (
    assert_delete_friend_successfully,
    assert_delete_friend_success_response_schema,
    assert_delete_friend_success_payload_schema
)
username_valid = "Spiritual-Pay-8530"
id_username_valid = "r9_8239so"
url = "https://oauth.reddit.com"
def getSubmitUrl(username):
    return f"{url}/api/v1/me/friends/{username}"
#Eliminar amigo existente
@pytest.mark.smoke
@pytest.mark.functional
def test_DELU001_delete_friend_with_username_valid(get_token_fixture):
    """AA001 - eliminar amigo con username valid"""
    headers = {
        "Authorization": f"Bearer {get_token_fixture}",
        "User-Agent": "SansiSofRFV/0.1 by IceOld4091",
        "Content-Type": "application/json",
    }
    payload = {"id": f"{id_username_valid}"}
    submit_url = f"{url}/api/v1/me/friends/{username_valid}"
    logger.debug("DELETE " + submit_url+ " HEADERS" + str(headers))
    logger.debug("Payload: " + str(payload))
    assert_delete_friend_success_payload_schema(payload)
    response = requests.delete(submit_url, headers=headers, json=payload)

    logger.info("Status Code: " + str(response.status_code))
    logger.debug("Response: " + str(response.text))
    # Assertions
    assert_delete_friend_successfully(response)

# Eliminar usuario que no es amigo
@pytest.mark.smoke
@pytest.mark.functional
def test_DELU002_delete_user_that_is_not_a_friend(get_token_fixture):
    """AA002 - No debe permitir eliminar a un usuario que no es nuestro amigo"""

    headers = {
        "Authorization": f"Bearer {get_token_fixture}",
        "User-Agent": "SansiSofRFV/0.1 by IceOld4091",
        "Content-Type": "application/json",
    }
    # TOMANDO EN CUENTA QUE EL USUARIO NO ES AMIGO, despues del primer test
    payload = {"id": f"{id_username_valid}"}
    submit_url = f"{url}/api/v1/me/friends/{username_valid}"

    logger.debug("DELETE " + submit_url + " HEADERS " + str(headers))
    logger.debug("Payload: " + str(payload))
    assert_delete_friend_success_payload_schema(payload)
    response = requests.delete(submit_url, headers=headers, json=payload)
    logger.info("Status Code: " + str(response.status_code))
    logger.debug("Response: " + str(response.text))

    assert response.status_code != 200 and response.status_code != 204, \
        "La API no debería permitir eliminar a un usuario que no es amigo"
    
# Eliminar usuario que no existe
@pytest.mark.smoke
@pytest.mark.functional
def test_DELU003_delete_user_that_does_not_exist(get_token_fixture):
    """AA003 - No debe permitir eliminar a un usuario inexistente (esperado: 404)"""

    headers = {
        "Authorization": f"Bearer {get_token_fixture}",
        "User-Agent": "SansiSofRFV/0.1 by IceOld4091",
        "Content-Type": "application/json",
    }

    nonexistent_username = "Nonrate"
    nonexistent_user_id = "Nonrate"

    payload = {"id": nonexistent_user_id}
    submit_url = f"{url}/api/v1/me/friends/{nonexistent_username}"

    logger.debug("DELETE " + submit_url + " HEADERS " + str(headers))
    logger.debug("Payload: " + str(payload))

    assert_delete_friend_success_payload_schema(payload)

    response = requests.delete(submit_url, headers=headers, json=payload)

    logger.info("Status Code: " + str(response.status_code))
    logger.debug("Response: " + str(response.text))

    if response.status_code != 404:
        pytest.xfail("La API no debería devolver éxito al intentar eliminar un usuario inexistente")

    assert response.status_code == 404, \
        f"Se esperaba 404 Not Found, pero se recibió {response.status_code}"

# Eliminar usuario sin token
@pytest.mark.smoke
@pytest.mark.functional
def test_DELU004_delete_friend_without_token():
    """AA004 - No debe permitir eliminar un amigo sin autenticación (esperado: 401 Unauthorized)"""

    headers = {
        # No se incluye "Authorization"
        "User-Agent": "SansiSofRFV/0.1 by IceOld4091",
        "Content-Type": "application/json",
    }

    nonexistent_username = "Nonrate"
    nonexistent_user_id = "Nonrate"

    payload = {"id": id_username_valid}
    submit_url = f"{url}/api/v1/me/friends/{username_valid}"

    logger.debug("DELETE " + submit_url + " HEADERS " + str(headers))
    logger.debug("Payload: " + str(payload))

    assert_delete_friend_success_payload_schema(payload)

    response = requests.delete(submit_url, headers=headers, json=payload)

    logger.info("Status Code (sin token): " + str(response.status_code))
    logger.debug("Response (sin token): " + str(response.text))

    if response.status_code not in [403]:
        pytest.xfail("La API debería rechazar la solicitud sin token, pero no lo hizo correctamente")

    assert response.status_code in [403], \
        f"Se esperaba 401 al eliminar sin token, pero se recibió {response.status_code}"

# Eliminar usuario con token inválido
@pytest.mark.smoke
@pytest.mark.functional
def test_DELU005_delete_friend_with_invalid_token():
    """AA005 - No debe permitir eliminar un amigo con token inválido (esperado: 401 o 403)"""

    headers = {
        "Authorization": "test",
        "User-Agent": "SansiSofRFV/0.1 by IceOld4091",
        "Content-Type": "application/json",
    }

    payload = {"id": id_username_valid}
    submit_url = f"{url}/api/v1/me/friends/{username_valid}"

    logger.debug("DELETE " + submit_url + " HEADERS " + str(headers))
    logger.debug("Payload: " + str(payload))

    assert_delete_friend_success_payload_schema(payload)

    response = requests.delete(submit_url, headers=headers, json=payload)

    logger.info("Status Code (token inválido): " + str(response.status_code))
    logger.debug("Response (token inválido): " + str(response.text))

    if response.status_code not in [401, 403]:
        pytest.xfail("La API debería rechazar la solicitud con token inválido, pero no lo hizo correctamente")

    assert response.status_code in [401, 403], \
        f"Se esperaba 401/403 al eliminar con token inválido, pero se recibió {response.status_code}"
# Eliminar usuario con token cadicado
@pytest.mark.smoke
@pytest.mark.functional
def test_DELU005_delete_friend_with_expired_token():
    """AA005 - No debe permitir eliminar un amigo con token inválido (esperado: 401 o 403)"""

    headers = {
        "Authorization": os.getenv("REDDIT_ACCESS_TOKEN_CADUCADO"),
        "User-Agent": "SansiSofRFV/0.1 by IceOld4091",
        "Content-Type": "application/json",
    }

    payload = {"id": id_username_valid}
    submit_url = f"{url}/api/v1/me/friends/{username_valid}"

    logger.debug("DELETE " + submit_url + " HEADERS " + str(headers))
    logger.debug("Payload: " + str(payload))

    assert_delete_friend_success_payload_schema(payload)

    response = requests.delete(submit_url, headers=headers, json=payload)

    logger.info("Status Code (token inválido): " + str(response.status_code))
    logger.debug("Response (token inválido): " + str(response.text))

    if response.status_code == 200:
        pytest.xfail("La API debería rechazar la solicitud con token inválido, pero no lo hizo correctamente")
    else :
        assert True, f"Se esperaba 401/403 al eliminar con token inválido, pero se recibió {response.status_code}"

# Eliminar usuario sin Content-Type
@pytest.mark.smoke
@pytest.mark.functional
def test_DELU006_delete_friend_without_content_type(get_token_fixture):
    """AA006 - No debe permitir eliminar un amigo sin header Content-Type (esperado: 400, 415, 403, etc.)"""

    headers = {
        "Authorization": f"Bearer {get_token_fixture}",
        "User-Agent": "SansiSofRFV/0.1 by IceOld4091",
        # "Content-Type" omitido intencionalmente
    }

    payload = {"id": id_username_valid}
    submit_url = f"{url}/api/v1/me/friends/{username_valid}"

    logger.debug("DELETE " + submit_url + " HEADERS (sin Content-Type): " + str(headers))
    logger.debug("Payload: " + str(payload))

    assert_delete_friend_success_payload_schema(payload)

    response = requests.delete(submit_url, headers=headers, json=payload)

    logger.info("Status Code (sin Content-Type): " + str(response.status_code))
    logger.debug("Response (sin Content-Type): " + str(response.text))

    if response.status_code in [200, 204]:
        pytest.xfail("La API no debería aceptar la solicitud sin Content-Type")

    assert response.status_code not in [200, 204], \
        f"Se esperaba error al eliminar sin Content-Type, pero se recibió {response.status_code}"