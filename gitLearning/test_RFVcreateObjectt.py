import json
import pytest
import requests
import jsonschema
from jsonschema import validate

input_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "data": {
            "type": "object",
            "properties": {
                "year": {"type": "integer"},
                "price": {"type": "number"},
                "CPU model": {"type": "string"},
                "Hard disk size": {"type": "string"}
            },
            "required": ["year", "price", "CPU model", "Hard disk size"]
        }
    },
    "required": ["name", "data"]
}

output_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "createdAt": {"type": "string"},
        "data": {
            "type": "object",
            "properties": {
                "year": {"type": "integer"},
                "price": {"type": "number"},
                "CPU model": {"type": "string"},
                "Hard disk size": {"type": "string"}
            },
            "required": ["year", "price", "CPU model", "Hard disk size"]
        }
    },
    "required": ["id", "name", "createdAt", "data"]
}

@pytest.mark.smoke
@pytest.mark.regression
def test_RFVcreateObject(get_url):
    """
    Este test verifica que se puede adicionar un objeto a la lista.
    También valida el esquema JSON del body y de la respuesta.
    """
    url = get_url + "/objects"
    
    payload = {
        "name": "Apple Diplo",
        "data": {
            "year": 2029,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        validate(instance=payload, schema=input_schema)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON body input schema don't match: {err}")

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    assert response.status_code == 200

    try:
        validate(instance=response.json(), schema=output_schema)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON response schema don't match: {err}")