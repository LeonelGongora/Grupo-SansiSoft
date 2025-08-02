import uuid
import pytest
import requests
from src.resources.payloads.create_subreddit_payload import get_create_subreddit_payload
from src.assertions.subreddit_assertions import (
    assert_subreddit_created_successfully,
    assert_subreddit_response_schema
)
BASE_URL = "https://oauth.reddit.com"
ENDPOINT = "/api/site_admin"
URL = BASE_URL + ENDPOINT


def generate_unique_name(base):
    return f"{base}_{uuid.uuid4().hex[:6]}"


@pytest.mark.smoke
def test_SCRUM_T41_Crear_un_subreddit_con_nombre_valido(get_token_fixture):
    base_url = "https://oauth.reddit.com"
    endpoint = "/api/site_admin"
    url = base_url + endpoint

    nombresubreddit = "ceniaprueba"
    payload = get_create_subreddit_payload(nombresubreddit)

    headers = {
        'Authorization': f'bearer {get_token_fixture}',
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "MiScriptQA/0.1"
    }

    response = requests.post(url, headers=headers, data=payload)
    print(response.status_code)
    print(response.text)

    assert_subreddit_created_successfully(response)
    assert_subreddit_response_schema(response.json())


