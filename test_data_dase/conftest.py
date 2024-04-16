import os
import psycopg2
import pytest
from dotenv import load_dotenv
from test_data.test_data import TestData


@pytest.fixture
def db_connection():
    """
        Фикстура для создания подключения к базе данных PostgreSQL.

        Returns:
            psycopg2.extensions.connection: Объект подключения к базе данных PostgreSQL.
    """
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


@pytest.fixture
def db_connection_db_postgres():
    """
        Фикстура для создания подключения к другой базе данных PostgreSQL.

        Returns:
            psycopg2.extensions.connection: Объект подключения к другой базе данных PostgreSQL.
    """
    connection = None
    load_dotenv()
    try:
        db_config = {
            "dbname": os.environ["OTHER_DBNAME"],
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


@pytest.fixture
def db_test_data():
    """
        Фикстура для создания тестовых данных.
    """
    return TestData()
