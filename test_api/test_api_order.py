import pytest
import allure
from allure import step
from conftest import api_fixture, test_data


@allure.title("Тест создания заказа на питомца")
@pytest.mark.parametrize("status", ["placed", "approved", "delivered"])
def test_create_order_for_pet(api_fixture, test_data, status):
    with step("Генерируем данные"):
        generated_data = test_data.generate_test_data()

    with step("Добавляем питомца и создаём заказ"):
        api_fixture.pet_store_pet.add_new_pet_store(test_data=generated_data, status=status)
        create_pet_order = api_fixture.pet_store_order.create_order_for_pet(test_data=generated_data, status=status)

    with step("Проверяем статус заказа"):
        assert create_pet_order["status"] == status


@allure.title("Тест поиска заказа по его идентификатору")
def test_find_purchase_order_id(api_fixture, test_data):
    with step("Генерируем данные"):
        generated_data = test_data.generate_test_data()

    with step("Добавляем питомца и создаём заказ"):
        api_fixture.pet_store_pet.add_new_pet_store(test_data=generated_data, status="available")
        create_pet_order = api_fixture.pet_store_order.create_order_for_pet(test_data=generated_data, status="approved")

    with step("Запрашиваем данные о заказе по его ID"):
        get_order_data = api_fixture.pet_store_order.get_find_purchase_order_id(id=create_pet_order["id"])

    with step("Проверяем статусы"):
        assert get_order_data[0]["status"] == "approved"
        assert get_order_data[0]["petId"] == generated_data.pet_data.id


@allure.title("Тест получения остатков по статусу")
def test_inventories_by_status(api_fixture):
    response_status_code = api_fixture.pet_store_order.get_inventories_by_status()
    assert response_status_code[1] == 200


@allure.title("Тест удаления заказа")
def test_delete_order(test_data, api_fixture):
    with step("Генерируем данные"):
        pet_test_data = test_data.generate_test_data()

    with step("Добавляем питомца и создаём заказ"):
        api_fixture.pet_store_pet.add_new_pet_store(test_data=pet_test_data, status="approved")
        api_fixture.pet_store_order.create_order_for_pet(test_data=pet_test_data, status="approved")

    with step("Удаляем заказ"):
        order_delete = api_fixture.pet_store_order.order_delete(orderId=pet_test_data.order_data.id)

    with step("Проверяем статусы"):
        assert order_delete == 200
