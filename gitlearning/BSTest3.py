import requests

# -*- coding: utf-8 -*-
# Test que simula un error 400 Bad Request enviando una URL malformada
def test_bad_request():
    url = "https://pokeapi.co/api/v2/pokemon/%%%"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    assert response.status_code == 400