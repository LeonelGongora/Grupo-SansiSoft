import pytest
import requests
from dotenv import load_dotenv
load_dotenv()
from src.services.auth import get_token
from src.resources.helpers.create_post import create_post

@pytest.fixture(scope="session")
def get_token_fixture():
    return get_token()

@pytest.fixture(scope="session")
def created_post_id():
    return create_post(
    token=get_token(),
    title="Mi publicacion para mis test de prueba",
    text="Este texto lo escribo para todos los tests de prueba"
    )
