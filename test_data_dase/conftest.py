import os
import socket
import psycopg2
import pytest
from dotenv import load_dotenv


@pytest.fixture
def db_connection():
    if not is_local_machine():
        pytest.skip("Fixture skipped: Not running on local machine")

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
        yield connection
    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL:", ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")


def is_local_machine():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("127.0.0.1", 1))
        return True
    except socket.error:
        return False
    finally:
        s.close()
