import requests
import pytest

def test_artic_api_response_ok():
    url = "https://api.artic.edu/api/v1/artworks"
    params = {
        "fields": "id,title,artist_display,date_display,main_reference_number"
    }

    response = requests.get(url, params=params)

    assert response.status_code == 200

    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)

    if data["data"]:
        item = data["data"][0]
        for field in ["id", "title", "artist_display", "date_display", "main_reference_number"]:
            assert field in item

