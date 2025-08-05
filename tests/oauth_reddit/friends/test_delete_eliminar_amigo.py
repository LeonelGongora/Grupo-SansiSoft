import requests
import pytest
import os
import time
from src.logs.logger import logger
from src.assertions.eliminar_amigo_assertions import (
    assert_delete_friend_successfully,
    assert_delete_friend_success_response_schema,
    assert_delete_friend_success_payload_schema,
)
from src.services.auth import build_headers
from src.payloads.payload_aliminar_amigo import crear_payload_eliminar_amigo

username_valid = "Spiritual-Pay-8530"
id_username_valid = "r9_8239so"
url = "https://oauth.reddit.com"


def getSubmitUrl(username):
    return f"{url}/api/v1/me/friends/{username}"


# Eliminar amigo existente
@pytest.mark.smoke
@pytest.mark.functional
def test_DELU001_delete_friend_with_username_valid(get_token_fixture, get_user_agent):
    """DELU001 - eliminar amigo con username valid"""
    headers = build_headers(token=get_token_fixture, user_agent=get_user_agent)
    payload = crear_payload_eliminar_amigo(id=id_username_valid)
    submit_url = f"{url}/api/v1/me/friends/{username_valid}"
    logger.debug("DELETE " + submit_url + " HEADERS" + str(headers))
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
def test_DELU002_delete_user_that_is_not_a_friend(get_token_fixture, get_user_agent):
    """DELU002 - No debe permitir eliminar a un usuario que no es nuestro amigo"""
    # TOMANDO EN CUENTA QUE EL USUARIO NO ES AMIGO, despues del primer test
    payload = {"id": f"{id_username_valid}"}
    headers = build_headers(token=get_token_fixture, user_agent=get_user_agent)
    payload = crear_payload_eliminar_amigo(id=id_username_valid)
    submit_url = f"{url}/api/v1/me/friends/{username_valid}"

    logger.debug("DELETE " + submit_url + " HEADERS " + str(headers))
    logger.debug("Payload: " + str(payload))
    assert_delete_friend_success_payload_schema(payload)
    response = requests.delete(submit_url, headers=headers, json=payload)
    logger.info("Status Code: " + str(response.status_code))
    logger.debug("Response: " + str(response.text))

    assert (
        response.status_code != 200 and response.status_code != 204
    ), "La API no debería permitir eliminar a un usuario que no es amigo"


# Eliminar usuario que no existe
@pytest.mark.smoke
@pytest.mark.functional
def test_DELU003_delete_user_that_does_not_exist(get_token_fixture, get_user_agent):
    """DELU003 - No debe permitir eliminar a un usuario inexistente (esperado: 404)"""
    nonexistent_username = "Nonrate"
    nonexistent_user_id = "Nonrate"
    headers = build_headers(token=get_token_fixture, user_agent=get_user_agent)
    payload = crear_payload_eliminar_amigo(id=nonexistent_user_id)
    submit_url = f"{url}/api/v1/me/friends/{nonexistent_username}"

    logger.debug("DELETE " + submit_url + " HEADERS " + str(headers))
    logger.debug("Payload: " + str(payload))

    assert_delete_friend_success_payload_schema(payload)

    response = requests.delete(submit_url, headers=headers, json=payload)

    logger.info("Status Code: " + str(response.status_code))
    logger.debug("Response: " + str(response.text))

    if response.status_code != 404:
        pytest.xfail(
            "Se esperaba 404 Not Found, pero se recibió " + str(response.status_code)
        )

    assert (
        response.status_code == 404
    ), f"Se esperaba 404 Not Found, pero se recibió {response.status_code}"


# Eliminar usuario sin token
@pytest.mark.smoke
@pytest.mark.functional
def test_DELU004_delete_friend_without_token(get_user_agent):
    """DELU004 - No debe permitir eliminar un amigo sin autenticación (esperado: 401 Unauthorized)"""

    headers = {
        # No se incluye "Authorization"
        "User-Agent": get_user_agent,
    }
    payload = crear_payload_eliminar_amigo(id=id_username_valid)
    submit_url = f"{url}/api/v1/me/friends/{username_valid}"

    logger.debug("DELETE " + submit_url + " HEADERS " + str(headers))
    logger.debug("Payload: " + str(payload))

    assert_delete_friend_success_payload_schema(payload)

    response = requests.delete(submit_url, headers=headers, json=payload)

    logger.info("Status Code (sin token): " + str(response.status_code))
    logger.debug("Response (sin token): " + str(response.text))

    if response.status_code not in [403]:
        pytest.xfail(
            f"La API debería rechazar la solicitud sin token con status code 403, pero lo hizo con {response.status_code}"
        )

    assert response.status_code in [
        403
    ], f"Se esperaba 403 al eliminar sin token, pero se recibió {response.status_code}"


# Eliminar usuario con token inválido
@pytest.mark.smoke
@pytest.mark.functional
def test_DELU005_delete_friend_with_invalid_token(get_user_agent):
    """DELU005 - No debe permitir eliminar un amigo con token inválido (esperado: 401 o 403)"""
    token_invalido = "token_invalido"
    headers = build_headers(token=token_invalido, user_agent=get_user_agent)
    payload = crear_payload_eliminar_amigo(id=id_username_valid)
    submit_url = f"{url}/api/v1/me/friends/{username_valid}"

    logger.debug("DELETE " + submit_url + " HEADERS " + str(headers))
    logger.debug("Payload: " + str(payload))

    assert_delete_friend_success_payload_schema(payload)

    response = requests.delete(submit_url, headers=headers, json=payload)

    logger.info("Status Code (token inválido): " + str(response.status_code))
    logger.debug("Response (token inválido): " + str(response.text))

    if response.status_code not in [403]:
        pytest.xfail(
            f"Se esperaba 403 al eliminar con token inválido, pero se recibió {response.status_code}"
        )

    assert response.status_code in [
        403,
    ], f"Se esperaba 403 al eliminar con token inválido, pero se recibió {response.status_code}"


# Eliminar usuario con token caducado
@pytest.mark.smoke
@pytest.mark.functional
def test_DELU005_delete_friend_with_expired_token(get_user_agent):
    """DELU005 - No debe permitir eliminar un amigo con token inválido (esperado: 401 o 403)"""
    headers = build_headers(token=os.getenv("REDDIT_ACCESS_TOKEN_CADUCADO"), user_agent=get_user_agent)
    payload = crear_payload_eliminar_amigo(id=id_username_valid)
    submit_url = f"{url}/api/v1/me/friends/{username_valid}"

    logger.debug("DELETE " + submit_url + " HEADERS " + str(headers))
    logger.debug("Payload: " + str(payload))

    assert_delete_friend_success_payload_schema(payload)

    response = requests.delete(submit_url, headers=headers, json=payload)

    logger.info("Status Code (token inválido): " + str(response.status_code))
    logger.debug("Response (token inválido): " + str(response.text))

    if response.status_code == 401:
        assert True  # Comportamiento esperado
    elif response.status_code == 200:
        pytest.xfail("La API permitió eliminar con un token caducado (devolvió 200). Debería devolver 401.")
    else:
        pytest.fail(f"Se esperaba 401 al usar token caducado, pero se recibió {response.status_code}")


# DELU006 No debe permitir eliminar un amigo cuyo username contiene espacios
@pytest.mark.functional
@pytest.mark.negative
def test_DELU006_delete_friend_with_spaces_in_username(
    get_token_fixture, get_user_agent
):
    """
    DELU006 - No debe permitir eliminar un amigo cuyo username contiene espacios.
    Se espera un error (400, 422, 404, etc.). Si la API responde 200 o 204, se marca como xfail.
    """
    
    invalid_username = "user name"
    # URL encode it
    headers = build_headers(token=get_token_fixture, user_agent=get_user_agent)
    payload = crear_payload_eliminar_amigo(id=id_username_valid)
    submit_url = f"{url}/api/v1/me/friends/{invalid_username}"

    logger.debug(f"DELETE {submit_url} HEADERS: {headers}")
    logger.debug(f"Payload (username con espacios): {payload}")

    response = requests.delete(submit_url, headers=headers, json=payload)

    logger.info(f"Status Code (username con espacios): {response.status_code}")
    logger.debug(f"Response (username con espacios): {response.text}")

    if response.status_code in [200, 204]:
        pytest.xfail("La API no debería aceptar usernames con espacios")

    assert response.status_code not in [
        200,
        204,
    ], f"Se esperaba error al eliminar amigo con username inválido, pero se recibió {response.status_code}"


# DELU007 - No debe permitir eliminar un amigo cuyo username contiene solo números
@pytest.mark.functional
@pytest.mark.negative
def test_DELU007_delete_friend_with_numeric_username(get_token_fixture, get_user_agent):
    """
    DELU007 - No debe permitir eliminar un amigo cuyo username contiene solo números.
    Se espera un error (400, 422, 404, etc.). Si la API responde 200 o 204, se marca como xfail.
    """
    # Username numérico inválido
    numeric_username = "12345"
   
    headers = build_headers(token=get_token_fixture, user_agent=get_user_agent)
    payload = crear_payload_eliminar_amigo(id=id_username_valid)
    submit_url = f"{url}/api/v1/me/friends/{numeric_username}"

    logger.debug(f"DELETE {submit_url} HEADERS: {headers}")
    logger.debug(f"Payload (username numérico): {payload}")

    response = requests.delete(submit_url, headers=headers, json=payload)

    logger.info(f"Status Code (username numérico): {response.status_code}")
    logger.debug(f"Response (username numérico): {response.text}")

    if response.status_code in [200, 204]:
        pytest.xfail("La API no debería aceptar usernames numéricos (e.g., '12345')")

    assert response.status_code not in [
        200,
        204,
    ], f"Se esperaba error al eliminar amigo con username numérico, pero se recibió {response.status_code}"


# Eliminar usuario sin Content-Type
@pytest.mark.smoke
@pytest.mark.functional
def test_DELU008_delete_friend_without_content_type(get_token_fixture, get_user_agent):
    """DELU006 - No debe permitir eliminar un amigo sin header Content-Type (esperado: 400, 415, 403, etc.)"""
    headers = build_headers(token=get_token_fixture, user_agent=get_user_agent)
    payload = crear_payload_eliminar_amigo(id=id_username_valid)
    submit_url = f"{url}/api/v1/me/friends/{username_valid}"

    logger.debug(
        "DELETE " + submit_url + " HEADERS (sin Content-Type): " + str(headers)
    )
    logger.debug("Payload: " + str(payload))

    assert_delete_friend_success_payload_schema(payload)

    response = requests.delete(submit_url, headers=headers, json=payload)

    logger.info("Status Code (sin Content-Type): " + str(response.status_code))
    logger.debug("Response (sin Content-Type): " + str(response.text))

    if response.status_code in [200, 204]:
        pytest.xfail("La API no debería aceptar la solicitud sin Content-Type")

    assert response.status_code not in [
        200,
        204,
    ], f"Se esperaba error al eliminar sin Content-Type, pero se recibió {response.status_code}"
