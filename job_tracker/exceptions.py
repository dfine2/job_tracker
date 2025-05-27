import os


class InvalidDatabasePathException(Exception):
    def __init__(self):
        body = {"message": "Invalid database path. Please ensure that the DB_PATH enviroment variable is set.",
                "DB_PATH": os.getenv("DB_PATH", None) }
        super().__init__(body)