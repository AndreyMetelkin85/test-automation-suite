import allure
from allure import step
from conftest import test_data, api_fixture
from test_data.test_data import DataGenerator


@allure.feature("Добавление пользователя")
@allure.title("Проверяет создание пользователя в магазине домашних животных.")
def test_create_user(test_data, api_fixture):
    with step("Генерируем данные"):
        test_data = test_data.generate_test_data()

    with step("Создаём пользователя в системе"):
        user = api_fixture.pet_store_user.create_user(test_data=test_data, password="12345")

    with step("Сверяем статус"):
        assert user["code"] == 200


@allure.feature("Добавление пользователя")
@allure.title("Проверяет создание пользователей с использованием массива данных.")
def test_create_user_with_array(test_data, api_fixture):
    with step("Генерируем данные"):
        test_data_1 = DataGenerator().generate_test_data()
        test_data_2 = test_data.generate_test_data()

    with step("Добавляем нескольких пользователей"):
        user_array = api_fixture.pet_store_user.create_user_with_array(test_data_1=test_data_1,
                                                                       test_data_2=test_data_2,
                                                                       password="12345")

    with step("Сверяем статус"):
        assert user_array["code"] == 200


@allure.feature("Добавление пользователя")
@allure.title("Проверяет создание пользователя с использованием списка данных.")
def test_create_user_with_list(test_data, api_fixture):
    with step("Генерируем данные"):
        test_data = test_data.generate_test_data()

    with step("Добавляем пользователя через список"):
        user_array = api_fixture.pet_store_user.create_user_with_list(test_data=test_data, password="12345")

    with step("Сверяем статус"):
        assert user_array["code"] == 200


@allure.feature("Добавление пользователя")
@allure.title("Проверяет получение информации о пользователе по его имени.")
def test_get_user_name(test_data, api_fixture):
    with step("Генерируем данные"):
        test_data = test_data.generate_test_data()

    with step("Добавляем пользователя через список"):
        api_fixture.pet_store_user.create_user(test_data=test_data, password="12345")

    with step("Запрашиваем данные по имени пользователя"):
        user_name = api_fixture.pet_store_user.get_user_name(user_name=test_data.user.username)

    with step("Сверяем имя пользователя"):
        assert user_name[0]["username"] == test_data.user.username


@allure.feature("Добавление пользователя")
@allure.title("Проверяет обновление имени пользователя.")
def test_put_user_name(test_data, api_fixture):
    with step("Генерируем данные"):
        test_data = test_data.generate_test_data()
        new_user_name = DataGenerator().generate_test_data()

    with step("Добавляем пользователя"):
        api_fixture.pet_store_user.create_user(test_data=test_data, password="12345")

    with step("Добавляем пользователя"):
        new_username = api_fixture.pet_store_user.put_user_name(user_name=new_user_name.user.username,
                                                                test_data=test_data,
                                                                password="12345")

    with step("Сверяем статус"):
        assert new_username["code"] == 200


@allure.feature("Добавление пользователя")
@allure.title("Проверяет удаление пользователя.")
def test_user_delete(test_data, api_fixture):
    with step("Генерируем данные"):
        test_data = test_data.generate_test_data()

    with step("Добавляем пользователя"):
        api_fixture.pet_store_user.create_user(test_data=test_data, password="12345")

    with step("Удаляем пользователя"):
        user = api_fixture.pet_store_user.user_delete(user_name=test_data.user.username)

    with step("Сверяем статус"):
        assert user["code"] == 200


@allure.feature("Добавление пользователя")
@allure.title("Проверяет вход пользователя в систему.")
def test_user_login(test_data, api_fixture):
    with step("Генерируем данные"):
        test_data = test_data.generate_test_data()

    with step("Добавляем пользователя"):
        api_fixture.pet_store_user.create_user(test_data=test_data, password="12345")

    with step("Логинимся в системе"):
        user_login = api_fixture.pet_store_user.user_login(user_name=test_data.user.username, password="12345")

    with step("Сверяем статус"):
        assert user_login[0]["code"] == 200


@allure.feature("Добавление пользователя")
@allure.title("Проверяет выход пользователя из системы.")
def test_user_logout(test_data, api_fixture):
    with step("Генерируем данные"):
        test_data = test_data.generate_test_data()

    with step("Добавляем пользователя"):
        api_fixture.pet_store_user.create_user(test_data=test_data, password="12345")

    with step("Логинимся в системе"):
        api_fixture.pet_store_user.user_login(user_name=test_data.user.username, password="12345")

    with step("Выходим из системы"):
        user_logout = api_fixture.pet_store_user.user_log_out()

    with step("Сверяем статус"):
        assert user_logout[0]["code"] == 200
