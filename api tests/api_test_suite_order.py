import pytest

from conftest import pet_test_data, order_test_data, pet_store_pet_fixture, order_store_pet_fixture


# Тест создания заказа на питомца.
@pytest.mark.parametrize("status", ["placed", "approved", "delivered"])
def test_create_order_for_pet(pet_test_data, order_test_data, pet_store_pet_fixture, order_store_pet_fixture, status):
    pet_test_data = pet_test_data.pet_test_data()
    order_test_data = order_test_data.order_test_data()
    pet_store_pet_fixture.add_new_pet_store(pet_test_data=pet_test_data, status=status)
    create_pet_order = order_store_pet_fixture.create_order_for_pet(
        order_test_data=order_test_data, pet_test_data=pet_test_data, status=status)
    assert create_pet_order["status"] == status


# Тест поиска заказа по его идентификатору.
@pytest.mark.parametrize("id, expected_status", [(1, 404), (2, 200), (3, 404), (4, 200), (5, 200)])
def test_find_purchase_order_id(order_store_pet_fixture, id, expected_status):
    get_order_by_id, status_code = order_store_pet_fixture.get_find_purchase_order_id(id=id)
    assert status_code == expected_status


#  Тест получения остатков по статусу.
def test_inventories_by_status(order_store_pet_fixture):
    response_status_code = order_store_pet_fixture.get_inventories_by_status()
    assert response_status_code[1] == 200


# Тест удаления заказа.
def test_delete_order(pet_test_data, order_test_data, pet_store_pet_fixture, order_store_pet_fixture):
    pet_test_data = pet_test_data.pet_test_data()
    order_test_data = order_test_data.order_test_data()
    pet_store_pet_fixture.add_new_pet_store(pet_test_data=pet_test_data, status="approved")
    order_store_pet_fixture.create_order_for_pet(
        order_test_data=order_test_data, pet_test_data=pet_test_data, status="approved")
    order_delete = order_store_pet_fixture.order_delete(orderId=order_test_data["id"])
    assert order_delete["code"] == 200
