import requests

# Prioridad
# Media

def test_RF0001_obtener_noticias_con_palabra_clave_debate():
    """El usuario debe obtener una lista de noticias de The Guardian que contengan la palabra clave “debate” en la página 2."""

 
    url = "https://content.guardianapis.com/search?page=2&q=debate&api-key=test"

    payload = {}
    headers = {
  'Cookie': 'AWSALB=SU1EnV4H8lOuBqnwVniSq9if5vFtQ3gTLX4+vYmJ6j49dFNJYiNaUtJmWp/cNQ3YPyNEYeuy/Wb82DK/5d74usX77fChGchdgc3n8tEbH4yowMNr+td6CarWYo/5; AWSALBCORS=SU1EnV4H8lOuBqnwVniSq9if5vFtQ3gTLX4+vYmJ6j49dFNJYiNaUtJmWp/cNQ3YPyNEYeuy/Wb82DK/5d74usX77fChGchdgc3n8tEbH4yowMNr+td6CarWYo/5'
}
    response = requests.get(url, headers=headers, data=payload)

    assert response.status_code == 200

    json_data = response.json()
    assert "response" in json_data
    assert json_data["response"]["status"] == "ok"
    assert isinstance(json_data["response"]["results"], list)


