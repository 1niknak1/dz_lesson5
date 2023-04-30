import os.path

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


JSON_SCHEMA_FILE_PATH = get_path(filename="users_schema.json")
JSON_FILE_PATH = get_path(filename="users_with_books.json")
