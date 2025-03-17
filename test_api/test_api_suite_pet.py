import pytest
import allure
from allure import step
from conftest import pet_store_pet_fixture, test_data


@allure.title("Проверяет добавление нового животного в магазин домашних животных.")
@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_add_new_pet_in_store(pet_store_pet_fixture, test_data, status):

    with step("Генерируем данные"):
        test_data = test_data.generate_test_data()

    with step("Добавляем животное"):
        add_new_pet = pet_store_pet_fixture.add_new_pet_store(test_data=test_data, status=status)

    with step("Сверяем статус"):
        assert add_new_pet["status"] == status


@allure.title("Тест для проверки обновления информации о питомце в зоомагазине.")
@pytest.mark.parametrize("status", ["pending", "sold"])
def test_updates_pet_store(pet_store_pet_fixture, test_data, status):

    with step("Генерируем данные"):
        test_data_pet = test_data.generate_test_data()
        new_name = test_data.generate_test_data()

    with step("Добавляем животное в и затем обновляем информацию о нём."):
        add_pet = pet_store_pet_fixture.add_new_pet_store(test_data=test_data_pet, status="available")
        update_pet = pet_store_pet_fixture.updates_pet_store(id=add_pet["id"], test_data=new_name, status=status)

    with step("Сверяем статус"):
        assert update_pet["code"] == 200


@allure.title("Тест для загрузки изображения питомца")
def test_upload_image_pet(pet_store_pet_fixture, test_data):

    with step("Генерируем данные"):
        test_data = test_data.generate_test_data()

    with step("Добавляем животное и загружаем фото"):
        pet_store_pet_fixture.add_new_pet_store(test_data=test_data, status="available")
        foto_pet = pet_store_pet_fixture.upload_image_pet(id=test_data.pet_data.id, metadata="Pet photo")

    with step("Сверяем статус"):
        assert foto_pet["code"] == 200


@allure.title("Тест для обновления существующего питомца")
def test_update_an_existing_pet(pet_store_pet_fixture, test_data):

    with step("Генерируем данные"):
        test_data_pet = test_data.generate_test_data()
        update_pet_data = test_data.generate_test_data()

    with step("Добавляем животное, затем обновляем данные"):
        pet_store_pet_fixture.add_new_pet_store(test_data=test_data_pet, status="available")
        new_pet_data = pet_store_pet_fixture.update_an_existing_pet(test_data=update_pet_data, status="pending")

    with step("Сверяем статус"):
        assert new_pet_data["id"] == update_pet_data.pet_data.id


@allure.title("Тест для получения информации о питомце по его идентификатору")
def test_get_pet_id(pet_store_pet_fixture, test_data):

    with step("Генерируем данные"):
        test_data = test_data.generate_test_data()

    with step("Добавляем животное в магазин"):
        pet_store_pet_fixture.add_new_pet_store(test_data=test_data, status="available")

    with step("Запрашиваем данные по ID питомца"):
        get_pet = pet_store_pet_fixture.get_pet_id(id=test_data.pet_data.id)

    with step("Сверяем статус"):
        assert get_pet[0]["id"] == test_data.pet_data.id


@allure.title("Тест проверяет, что метод get_finds_pets_by_status возвращает животных с указанным статусом")
@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_get_finds_pets_by_status(pet_store_pet_fixture, status):

    with step("Запрашиваем данные о питомцах по статусу"):
        found_pets = pet_store_pet_fixture.get_finds_pets_by_status(status=status)

    with step("Сверяем статус"):
        for pet in found_pets[0]:
            assert pet["status"] == status


@allure.title("Тест проверяет корректность удаления животного из магазина")
def test_pet_delete(pet_store_pet_fixture, test_data):

    with step("Генерируем данные"):
        test_data = test_data.generate_test_data()

    with step("Добавляем животное в магазин"):
        add_pet = pet_store_pet_fixture.add_new_pet_store(test_data=test_data, status="available")

    with step("Удаляем питомца"):
        pet_delete = pet_store_pet_fixture.pet_delete(id=add_pet["id"])

    with step("Сверяем статус"):
        assert pet_delete["code"] == 200
