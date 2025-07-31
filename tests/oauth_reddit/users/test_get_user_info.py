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

@pytest.mark.functional
def test_OI_002_obtener_info_usuario_sin_autentificacion():
    
    """Descripción: Se intenta informacion de un usuario, eliminando el header Authorization en los headers que se envia"""

    username_objetivo = os.getenv("REDDIT_USERNAME_VALIDO") # Usuario inexistente

    headers = {
        "User-Agent": os.getenv("REDDIT_USER_AGENT")  # Se borra header Authorization
    }

    url = f"https://oauth.reddit.com/user/{username_objetivo}/about"
    response = requests.get(url, headers=headers)

    assert response.status_code == 200

@pytest.mark.functional
def test_OI_003_obtener_info_usuario_inexistente(get_token_fixture):

    """Descripción: Se intenta informacion de un usuario, utilizando un nombre de usuario que no pertenece a ningun usuario registrado de Reddit"""

    username_objetivo = os.getenv("REDDIT_USERNAME_INEXISTENTE") # Usuario inexistente
    access_token = get_token_fixture  

    headers = {
        "Authorization": f"bearer {access_token}",
        "User-Agent": os.getenv("REDDIT_USER_AGENT")
    }

    url = f"https://oauth.reddit.com/user/{username_objetivo}/about"
    response = requests.get(url, headers=headers)

    assert response.status_code == 200

@pytest.mark.functional
def test_OI_004_obtener_info_usuario_con_caracteres_especiales(get_token_fixture):
    
    """Descripción: Se intenta informacion de un usuario, utilizando un nombre de usuario con contiene caracteres especiales,
    lo cual infringe las normas de Reddit para nombrar los nombres de usuario"""

    username_objetivo = os.getenv("REDDIT_USERNAME_CARACTERES_ESPECIALES") # Nombre de usuario con caracteres especiales
    access_token = get_token_fixture  

    headers = {
        "Authorization": f"bearer {access_token}",
        "User-Agent": os.getenv("REDDIT_USER_AGENT")
    }

    url = f"https://oauth.reddit.com/user/{username_objetivo}/about"
    response = requests.get(url, headers=headers)

    assert response.status_code == 200
