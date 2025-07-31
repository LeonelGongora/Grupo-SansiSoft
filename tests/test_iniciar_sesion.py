import time
import pytest
from src.configuration.config import RedditAuthConfig



def test001_iniciar_sesion():
    auth = RedditAuthConfig(refresh_buffer=60)
    token = auth.get_token()

    assert token is not None, "El token no debería ser None"
    assert isinstance(token, str), "El token debe ser un string"
    assert len(token) > 0, "El token debe tener contenido"
    assert auth._token_expiry > time.time(), "La expiración del token debe estar en el futuro"