import json
from jsonschema import validate

from hw import JSON_SCHEMA_FILE_PATH, JSON_FILE_PATH


def assert_valid_schema(validate_file, schema_file):
    with open(validate_file) as f:
        validate_me = json.load(f)
    with open(schema_file) as f:
        schema = json.load(f)
    return validate(instance=validate_me, schema=schema)


def test_get_post():
    assert_valid_schema(JSON_SCHEMA_FILE_PATH, JSON_FILE_PATH)
