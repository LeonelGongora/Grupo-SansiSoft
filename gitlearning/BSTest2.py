import requests

# -*- coding: utf-8 -*-
# Se provoca un error 404 en la url para probar el manejo de errores
def test_get_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon/metapodd"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)

    assert response.status_code == 404
     # assert response.json() is not None
