import requests
from requests.auth import HTTPBasicAuth

def test_obtener_token():
    # Descripción: El objetivo es obtener el access token para obtener 
    # el acceso autorizado a los endpoints protegidos de la API.

    url = 'https://www.reddit.com/api/v1/access_token'

    username_auth = 'FNohpZB9fVWco0R9_zVRoQ'  # Client ID obtenido de la cuenta de Reddit
    password_auth = '8vjX79r84sDrJ_Fs3xnOeuLVB4NS9A'  # Client secret obtenido de la cuenta de Reddit

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'csv=2; edgebucket=qYkUkNtkZ1IScKdlBr; loid=0000000011chneogn5.2.1716952374778.Z0FBQUFBQm9oVFo5UnhVdHBSbC1ralZUVGRRTHFEVGlWTmpBN2tHNE1kTEIyZWR4Z0VzcXhCR1Qyck9VbnZTNlVmNXFIeVFCZlpTc1BEYWJqTlY2cEI4NVNhQUZiaHY4ak5ZVDZYOWh2WjBaeWVXX0hzalFTMEZjNldJd01fM2ZsLVFCZ3JuREpKSm4'
    }

    data = {
        'grant_type': 'password',   # Tipo de autentificacion
        'username': 'No_Apartment5800',  # El nombre de usuario de la cuenta de Reddit
        'password': 'strokes2500'  # La contraseña de la cuenta de Reddit
    }

    response = requests.post(
        url,
        headers=headers,
        data=data,
        auth=HTTPBasicAuth(username_auth, password_auth)
    )

    assert response.status_code == 200
    print(response.text)