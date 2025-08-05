from src.services.auth import build_headers
import requests

def test_validar_token_funciona():
    headers = build_headers()
    response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
    print("Código de respuesta:", response.status_code)
    print("Respuesta JSON:", response.json())
    assert response.status_code == 200
