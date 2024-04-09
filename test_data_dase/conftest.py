import psycopg2
import pytest

from config import DB_CONFIG


@pytest.fixture
def db_connection():
    connection = None
    try:
        connection = psycopg2.connect(**DB_CONFIG)
        yield connection
    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL:", ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")
