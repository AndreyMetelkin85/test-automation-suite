import os

import psycopg2
import pytest


@pytest.fixture
def db_connection():
    connection = None
    try:
        db_config = {
            "dbname": os.environ["dbname"],
            "user": os.environ["user"],
            "password": os.environ["password"],
            "host": os.environ["host"],
            "port": os.environ["port"]
        }
        connection = psycopg2.connect(**db_config)
        # connection = psycopg2.connect(**DB_CONFIG)
        yield connection
    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL:", ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")
