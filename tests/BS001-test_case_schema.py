

import json
import pytest
import requests
import jsonschema
from jsonschema import validate


input_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "data": {
      "type": "object",
      "properties": {
        "year": {
          "type": "integer"
        },
        "price": {
          "type": "number"
        },
        "CPU model": {
          "type": "string"
        },
        "Hard disk size": {
          "type": "string"
        }
      },
      "required": [
        "year",
        "price",
        "CPU model",
        "Hard disk size"
      ]
    }
  },
  "required": [
    "name",
    "data"
  ]
}

output_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "data": {
      "type": "object",
      "properties": {
        "year": {
          "type": "integer"
        },
        "price": {
          "type": "number"
        },
        "CPU model": {
          "type": "string"
        },
        "Hard disk size": {
          "type": "string"
        }
      },
      "required": [
        "year",
        "price",
        "CPU model",
        "Hard disk size"
      ]
    },
    "createdAt": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "name",
    "data",
    "createdAt"
  ]
}


def test_BS_create_computer():
    """
    Este test verifica que se pueda crear un computador
    """

    url = "https://api.restful-api.dev/objects"

    payload = {
        "name": "Computer Tarea Brandon",
        "data": {
            "year": 2020,
            "price": 1000,
            "CPU model": "Intel Core i7",
            "Hard disk size": "1TB"
        }
    }

    headers = {"Content-Type": "application/json"}

    try:
        validate(instance=payload,schema=input_schema)
    except jsonschema.exceptions.ValidationError as e:
        pytest.fail(f"Input schema validation failed: {e.message}")


    response = requests.post(url, data=json.dumps(payload), headers=headers)


    assert response.status_code == 200, f"Se esperaba un codigo 200 se recibe "f"{response.status_code}"

    try:
        validate(instance=response.json(), schema=output_schema)
    except jsonschema.exceptions.ValidationError as e:
        pytest.fail(f"Output schema validation failed: {e.message}")