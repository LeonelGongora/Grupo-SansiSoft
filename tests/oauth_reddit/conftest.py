import pytest
import os
from dotenv import load_dotenv
load_dotenv()
from src.services.auth import get_token
from src.redditApi.create_post import create_post

@pytest.fixture(scope="session")
def get_token_fixture():
    return get_token()

@pytest.fixture(scope="session")
def created_post_id():
    return create_post(
    token=get_token(),
    title='Hola amigos, como se levantaron hoy?',
    text="Este texto lo escribo para que lo lean",
    user_agent=os.getenv("REDDIT_USER_AGENT")
    )

@pytest.fixture(scope="session")
def get_user_agent():
    return os.getenv("REDDIT_USER_AGENT")