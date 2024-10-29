import allure
from conftest import test_data, pet_store_user_fixture
from qa_test_data.test_data import DataGenerator


# Проверяет создание пользователя в магазине домашних животных.
@allure.feature("add user")
def test_create_user(test_data, pet_store_user_fixture):
    test_data = test_data.generate_test_data()
    user = pet_store_user_fixture.create_user(test_data=test_data, password="12345")
    assert user["code"] == 200


# Проверяет создание пользователей с использованием массива данных.
@allure.feature("add user")
def test_create_user_with_array(test_data, pet_store_user_fixture):
    test_data_1 = DataGenerator().generate_test_data()
    test_data_2 = test_data.generate_test_data()
    user_array = pet_store_user_fixture.create_user_with_array(test_data_1=test_data_1,
                                                               test_data_2=test_data_2,
                                                               password="12345")
    assert user_array["code"] == 200


# Проверяет создание пользователя с использованием списка данных.
@allure.feature("add a user to the store system")
def test_create_user_with_list(test_data, pet_store_user_fixture):
    test_data = test_data.generate_test_data()
    user_array = pet_store_user_fixture.create_user_with_list(test_data=test_data, password="12345")
    assert user_array["code"] == 200


# Проверяет получение информации о пользователе по его имени.
@allure.feature("add a user to the store system")
def test_get_user_name(test_data, pet_store_user_fixture):
    test_data = test_data.generate_test_data()
    pet_store_user_fixture.create_user(test_data=test_data, password="12345")
    user_name = pet_store_user_fixture.get_user_name(user_name=test_data.user.username)
    assert user_name[0]["username"] == test_data.user.username


# Проверяет обновление имени пользователя.
@allure.feature("add a user to the store system")
def test_put_user_name(test_data, pet_store_user_fixture):
    test_data = test_data.generate_test_data()
    new_user_name = DataGenerator().generate_test_data()
    pet_store_user_fixture.create_user(test_data=test_data, password="12345")
    new_username = pet_store_user_fixture.put_user_name(user_name=new_user_name.user.username, test_data=test_data,
                                                        password="12345")
    assert new_username["code"] == 200


# Проверяет удаление пользователя.
@allure.feature("add a user to the store system")
def test_user_delete(test_data, pet_store_user_fixture):
    test_data = test_data.generate_test_data()
    pet_store_user_fixture.create_user(test_data=test_data, password="12345")
    user = pet_store_user_fixture.user_delete(user_name=test_data.user.username)
    assert user["code"] == 200


# Проверяет вход пользователя в систему.
@allure.feature("add a user to the store system")
def test_user_login(test_data, pet_store_user_fixture):
    test_data = test_data.generate_test_data()
    pet_store_user_fixture.create_user(test_data=test_data, password="12345")
    user_login = pet_store_user_fixture.user_login(user_name=test_data.user.username, password="12345")
    assert user_login[0]["code"] == 200


# Проверяет выход пользователя из системы.
@allure.feature("add a user to the store system")
def test_user_logout(test_data, pet_store_user_fixture):
    test_data = test_data.generate_test_data()
    pet_store_user_fixture.create_user(test_data=test_data, password="12345")
    pet_store_user_fixture.user_login(user_name=test_data.user.username, password="12345")
    user_logout = pet_store_user_fixture.user_log_out()
    assert user_logout[0]["code"] == 200
