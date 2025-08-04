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