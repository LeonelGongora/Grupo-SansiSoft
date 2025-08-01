import pytest
import requests
from dotenv import load_dotenv
load_dotenv()
from src.services.auth import get_token

@pytest.fixture(scope="session")
def get_token_fixture():
    return get_token()

