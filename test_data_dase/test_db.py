import pytest
from conftest import db_connection, db_connection_db_postgres


# Тест проверяет, что данные о самолете успешно извлекаются из базы данных по заданному коду.
@pytest.mark.db_test
@pytest.mark.parametrize("aircraft_code", [773, "CR2", 321])
def test_retrieve_aircraft_data_by_code(db_connection, aircraft_code):
    cursor = db_connection.cursor()
    sql_query = f"SELECT * FROM aircrafts_data WHERE aircraft_code = '{aircraft_code}'"
    cursor.execute(sql_query)
    result = cursor.fetchall()
    assert result, f"ID {aircraft_code} не найден в таблице"


# Тест проверяет, что данные о самолете успешно извлекаются из базы данных по заданному коду.
@pytest.mark.db_test
@pytest.mark.parametrize("range", [7900, 1200])
def test_get_aircraft_data_by_range(db_connection, range):
    cursor = db_connection.cursor()
    sql_query = f"SELECT * FROM aircrafts_data WHERE range = {range}"
    cursor.execute(sql_query)
    result = cursor.fetchall()
    assert result, f"range {range} не найден в таблице"


# Тест создает новую сущность в таблице базы данных "employees", затем проверяет,
# что созданная сущность присутствует в базе данных.
@pytest.mark.db_test
def test_create_entity_and_check(db_connection_db_postgres, db_test_data):
    db_test_data = db_test_data.db_test_data()
    cursor = db_connection_db_postgres.cursor()
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(255),
                last_name VARCHAR(255),
                department VARCHAR(255),
                position VARCHAR(255),
                phone VARCHAR(20),
                email VARCHAR(255)
            )
        """)
    db_connection_db_postgres.commit()

    cursor.execute(
        "INSERT INTO employees (first_name, last_name, department, position, phone, email) "
        "VALUES (%s, %s, %s, %s, %s, %s)",
        (db_test_data["first_name"],
         db_test_data["last_name"],
         db_test_data["department"],
         db_test_data["position"],
         db_test_data["phone"],
         db_test_data["email"]))
    db_connection_db_postgres.commit()

    cursor.execute(f"SELECT * "
                   f"FROM employees "
                   f"WHERE first_name = '{db_test_data['first_name']}' AND last_name = '{db_test_data['last_name']}'")

    result = cursor.fetchall()

    assert (db_test_data['first_name'], db_test_data['last_name']) in [(row[1], row[2]) for row in result], \
        "[INFO] Созданная сущность не найдена!!!"
