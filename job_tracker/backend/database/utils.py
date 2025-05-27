import os
import sqlite3

from job_tracker.exceptions import InvalidDatabasePathException

def get_db_conn() -> sqlite3.Connection:
    db_path = os.getenv("DB_PATH", None)
    if isinstance(db_path, str):
        conn = sqlite3.connect(db_path)
        return conn
    else:
        raise InvalidDatabasePathException()

    
