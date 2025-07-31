import requests
import pytest
import sys
import os
from dotenv import load_dotenv

# Agrega el directorio raíz del proyecto al path

load_dotenv()

@pytest.mark.smoke
@pytest.mark.functional
def test_OI_001_obtener_info_usuario_existente(get_token_fixture):

    """Descripción: Se obtiene la informacion de un usuario, utilizando un nombre de usuario existente"""

    username_objetivo = os.getenv("REDDIT_USERNAME_VALIDO")# Usuario existente
    access_token = get_token_fixture  # este viene del conftest.py

    headers = {
        "Authorization": f"bearer {access_token}",
        "User-Agent": os.getenv("REDDIT_USER_AGENT")
    }

    url = f"https://oauth.reddit.com/user/{username_objetivo}/about"
    response = requests.get(url, headers=headers)

    assert response.status_code == 200

