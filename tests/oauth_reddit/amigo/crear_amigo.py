import requests
import pytest
import os
import time
from src.assertions.amigo_assertions import (
    assert_add_friend_successfully,
    assert_add_friend_success_response_schema,
    assert_add_friend_success_payload_schema
)

@pytest.mark.smoke
@pytest.mark.functional
def test_AA001_add_friend(get_token_fixture):
    """AA001 - Add a friend successfully"""
    time.sleep(1)
    username = "Spiritual-Pay-8530"
    url = "https://oauth.reddit.com"
    headers = {
        "Authorization": f"Bearer {get_token_fixture}",
        "User-Agent": "SansiSofRFV/0.1 by IceOld4091",
        "Content-Type": "application/json",
    }
    payload = {"name": f"{username}"}
    assert_add_friend_success_payload_schema(payload)
    submit_url = f"{url}/api/v1/me/friends/{username}"
    response = requests.put(submit_url, headers=headers, json=payload)
    # Assertions
    assert_add_friend_successfully(response)
    assert_add_friend_success_response_schema(response.json())
