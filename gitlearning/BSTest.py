import requests
import pytest

# -*- coding: utf-8 -*-

def test_get_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon/metapod"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    assert response.json() is not None
    assert response.json()["name"] == "metapod"