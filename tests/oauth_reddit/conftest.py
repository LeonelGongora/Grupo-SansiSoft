import pytest
import requests
from dotenv import load_dotenv
load_dotenv()
import config as conf
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from auth import get_token

@pytest.fixture(scope="session")
def get_url():
    return conf.BASE_URL

@pytest.fixture(scope="session")
def get_token_fixture():
    return get_token()