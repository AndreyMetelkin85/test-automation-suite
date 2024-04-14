import os

import psycopg2
import pytest
from dotenv import load_dotenv


@pytest.fixture
def db_connection():
    connection = None
    load_dotenv()
    try:
        db_config = {
            "dbname": os.environ["DBNAME"],
            "user": os.environ["USER"],
            "password": os.environ["PASSWORD"],
            "host": os.environ["HOST"],
            "port": os.environ["PORT"]
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
