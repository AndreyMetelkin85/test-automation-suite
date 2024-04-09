import pytest

from test_data_dase.conftest import db_connection


@pytest.mark.parametrize("aircraft_code", [773, "CR2", 321])
def test_retrieve_aircraft_data_by_code(db_connection, aircraft_code):
    cursor = db_connection.cursor()
    sql_query = f"SELECT * FROM aircrafts_data WHERE aircraft_code = '{aircraft_code}'"
    cursor.execute(sql_query)
    result = cursor.fetchall()
    assert result, f"ID {aircraft_code} не найден в таблице"


@pytest.mark.parametrize("range", [7900, 1200])
def test_get_aircraft_data_by_range(db_connection, range):
    cursor = db_connection.cursor()
    sql_query = f"SELECT * FROM aircrafts_data WHERE range = {range}"
    cursor.execute(sql_query)
    result = cursor.fetchall()
    assert result, f"range {range} не найден в таблице"
