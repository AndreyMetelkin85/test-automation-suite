import pytest
from conftest import pet_store_pet_fixture


# Проверяет добавление нового животного в магазин домашних животных.
@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_add_new_pet_in_store(pet_store_pet_fixture, test_data, status):
    test_data = test_data.generate_test_data()
    add_new_pet = pet_store_pet_fixture.add_new_pet_store(test_data=test_data, status=status)
    assert add_new_pet["status"] == status


# Тест для проверки обновления информации о питомце в зоомагазине.
@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_updates_pet_store(pet_store_pet_fixture, test_data, status):
    test_data_pet = test_data.generate_test_data()
    new_name = test_data.generate_test_data()
    pet_store_pet_fixture.add_new_pet_store(test_data=test_data_pet, status=status)
    update_pet = pet_store_pet_fixture.updates_pet_store(id=test_data.pet_data.id, test_data=new_name, status=status)
    assert update_pet["code"] == 200


#  Тест для загрузки изображения питомца.
# @pytest.mark.skip("Тест падает при запуске в общем скоупе!")
def test_upload_image_pet(pet_store_pet_fixture, test_data):
    test_data = test_data.generate_test_data()
    pet_store_pet_fixture.add_new_pet_store(test_data=test_data, status="available")
    foto_pet = pet_store_pet_fixture.upload_image_pet(id=test_data.pet_data.id, metadata="Pet photo")
    assert foto_pet["code"] == 200


# Тест для обновления существующего питомца.
def test_update_an_existing_pet(pet_store_pet_fixture, test_data):

    test_data_pet = test_data.generate_test_data()
    pet_store_pet_fixture.add_new_pet_store(test_data=test_data_pet, status="available")
    new_pet_data = pet_store_pet_fixture.update_an_existing_pet(test_data=test_data, status="pending")
    assert new_pet_data["id"] == test_data.pet_data.id


# Тест для получения информации о питомце по его идентификатору.
def test_get_pet_id(pet_store_pet_fixture, test_data):
    test_data = test_data.generate_test_data()
    pet_store_pet_fixture.add_new_pet_store(test_data=test_data, status="available")
    get_pet = pet_store_pet_fixture.get_pet_id(id=test_data.pet_data.id)
    assert get_pet[0]["id"] == test_data.pet_data.id


# Тест проверяет, что метод get_finds_pets_by_status возвращает животных с указанным статусом.
@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_get_finds_pets_by_status(pet_store_pet_fixture, status):
    found_pets = pet_store_pet_fixture.get_finds_pets_by_status(status=status)
    for pet in found_pets[0]:
        assert pet["status"] == status


#  Тест проверяет корректность удаления животного из магазина.
def test_pet_delete(pet_store_pet_fixture, test_data):
    test_data = test_data.generate_test_data()
    pet_store_pet_fixture.add_new_pet_store(test_data=test_data, status="available")
    pet_delete = pet_store_pet_fixture.pet_delete(id=test_data.pet_data.id)
    assert pet_delete["code"] == 200
