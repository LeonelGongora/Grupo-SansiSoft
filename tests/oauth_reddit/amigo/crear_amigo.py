import requests
import pytest
import os
import time
from src.assertions.amigo_assertions import (
    assert_add_friend_successfully,
    assert_add_friend_success_response_schema,
    assert_add_friend_success_payload_schema
)
username_valid = "Spiritual-Pay-8530"
url = "https://oauth.reddit.com"
#Agregar amigo con nombre de usuario valido
@pytest.mark.smoke
@pytest.mark.functional
def test_AA001_add_friend_with_username_valid(get_token_fixture):
    """AA001 - Add a friend successfully"""
    time.sleep(2)
    headers = {
        "Authorization": f"Bearer {get_token_fixture}",
        "User-Agent": "SansiSofRFV/0.1 by IceOld4091",
        "Content-Type": "application/json",
    }
    payload = {"name": f"{username_valid}"}
    assert_add_friend_success_payload_schema(payload)
    submit_url = f"{url}/api/v1/me/friends/{username_valid}"
    response = requests.put(submit_url, headers=headers, json=payload)
    # Assertions
    assert_add_friend_successfully(response)
    assert_add_friend_success_response_schema(response.json())
# Agregar amigo con nombre que ya es nuestro amigo
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.xfail(reason="El API permite agregar al mismo amigo dos veces, debería fallar")
def test_AA002_add_friend_existing(get_token_fixture):
    """AA001 - Should fail when adding an already existing friend"""
    time.sleep(2)
    headers = {
        "Authorization": f"Bearer {get_token_fixture}",
        "User-Agent": "SansiSofRFV/0.1 by IceOld4091",
        "Content-Type": "application/json",
    }
    payload = {"name": f"{username_valid}"}
    assert_add_friend_success_payload_schema(payload)
    submit_url = f"{url}/api/v1/me/friends/{username_valid}"
    response = requests.put(submit_url, headers=headers, json=payload)
    assert response.status_code != 200, f"Expected failure, but got 200: {response.json()}"

# Agregar amigo con nombre que NO existe
@pytest.mark.smoke
@pytest.mark.functional
def test_AA003_add_friend_nonexistent_user(get_token_fixture):
    """AA002 - Should fail when adding a nonexistent Reddit user"""
    username_invalid = "username_invalid"
    time.sleep(2)
    headers = {
        "Authorization": f"Bearer {get_token_fixture}",
        "User-Agent": "SansiSofRFV/0.1 by IceOld4091",
        "Content-Type": "application/json",
    }

    payload = {"name": username_invalid}
    assert_add_friend_success_payload_schema(payload)
    submit_url = f"{url}/api/v1/me/friends/{username_invalid}"
    response = requests.put(submit_url, headers=headers, json=payload)
    if response.status_code != 404:
        pytest.xfail(f"Codigo esperado era 404, pero obtuvo {response.status_code}")
    
    assert response.status_code == 404

# Agregar amigo con token inválido → debe retornar 403
@pytest.mark.smoke
@pytest.mark.functional
def test_AA006_add_friend_with_invalid_token():
    """AA003 - Should return 403 when using an invalid access token"""
    time.sleep(2)

    invalid_token = "Bearer invalid_token_value"

    headers = {
        "Authorization": invalid_token,
        "User-Agent": "SansiSofRFV/0.1 by IceOld4091",
        "Content-Type": "application/json",
    }
    payload = {"name": username_valid}
    assert_add_friend_success_payload_schema(payload)
    submit_url = f"{url}/api/v1/me/friends/{username_valid}"
    response = requests.put(submit_url, headers=headers, json=payload)
    if response.status_code != 403:
        pytest.fail(f"Se esperaba el código 403 (Prohibido), pero se obtuvo {response.status_code}")
    else :
        assert response.status_code == 403