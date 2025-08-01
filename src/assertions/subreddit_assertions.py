import jsonschema
import pytest
import json
from src.resources.schemas import create_subreddit_response_schema

def assert_subreddit_created_successfully(response):
    assert response.status_code == 200, "No se pudo crear el subreddit"

def assert_subreddit_response_schema(response_json):
    schema = create_subreddit_response_schema.get_schema()
    try:
        jsonschema.validate(instance=response_json, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema no coincide: {err}")
