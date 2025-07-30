import pytest
import requests
import jsonschema

@pytest.mark.smoke
def test_004_Crear_un_nuevo_marca_de_celular():
    """ Verificar que se pueda crear una nueva marca de celular con
    su respectiva informacion como:"id","name","data": , "Capacity":,
    "year","price","CPU model" "Hard disk size"."""^""

    base_url = "https://api.restful-api.dev"
    endpoint = "/objects"
    url = base_url + endpoint

    payload = {
        "name": "prueba 10",
        "data": { "year": 2019,
                  "price": 1849.99,
                  "CPU model": "Intel Core i9",
                  "Hard disk size": "1 TB" }
    }

    headers = {
        "Content-Type": "application/json"
    }


    response = requests.post(url, headers=headers, json=payload)

    print(response.status_code)
    print(response.text)

    assert response.status_code == 200, "No se pudo crear la publicación"


    schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "createdAt": {
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
    "id",
    "name",
    "createdAt",
    "data"
  ]
}

    try:
        jsonschema.validate(instance=response.json(), schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema no coincide: {err}")