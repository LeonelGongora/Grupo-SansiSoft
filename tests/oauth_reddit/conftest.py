import pytest
import requests
import config as conf
from auth import get_auth_headers

@pytest.fixture(scope="session")
def get_url():
    return conf.BASE_URL

@pytest.fixture(scope="session")
def get_token():
    return get_auth_headers()