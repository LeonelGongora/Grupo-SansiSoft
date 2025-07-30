import requests
import jsonschema 

def test_add_object():
   
    url = "https://api.restful-api.dev/objects"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "name": "Test Device",
        "data": {
            "year": 2024,
            "price": 10000, 
            "cpu MODEL": "Intel codre i9",
            "Hard disk size" : "1 TB"
        }
    }

    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 200
    respuesta_json = response.json()

    scheme = {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "title": "Generated schema for Root",
            "type": "object",
            "properties": {
                "name": {
                "type": "string"
                },
                "data": {
                "type": "object",
                "properties": {
                    "year": {
                    "type": "number"
                    },
                    "price": {
                    "type": "number"
                    },
                    "cpu MODEL": {
                    "type": "string"
                    },
                    "Hard disk size": {
                    "type": "string"
                    }
                },
                "required": [
                    "year",
                    "price",
                    "cpu MODEL",
                    "Hard disk size"
                ]
                }
            },
            "required": [
                "name",
                "data"
            ]
            }
    try:
        jsonschema.validate(instance=respuesta_json, schema=scheme)
    except jsonschema.ValidationError as e:
        assert False, f"Schema validation error: {e.message}"
    

    

