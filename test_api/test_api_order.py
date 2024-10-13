import pytest
from conftest import pet_store_pet_fixture, order_store_pet_fixture, test_data


# Тест создания заказа на питомца.
@pytest.mark.parametrize("status", ["placed", "approved", "delivered"])
def test_create_order_for_pet(pet_store_pet_fixture, order_store_pet_fixture, test_data, status):
    generated_data = test_data.generate_test_data()
    pet_store_pet_fixture.add_new_pet_store(test_data=generated_data, status=status)
    create_pet_order = order_store_pet_fixture.create_order_for_pet(test_data=generated_data, status=status)
    assert create_pet_order["status"] == status


# Тест поиска заказа по его идентификатору.
@pytest.mark.parametrize("id, expected_status",
        [(1, (200, 404)), (2, (200, 404)), (3, (200, 404)), (4, (200, 404)), (5, (200, 404))])
def test_find_purchase_order_id(order_store_pet_fixture, id, expected_status):
    get_order_by_id, status_code = order_store_pet_fixture.get_find_purchase_order_id(id=id)
    assert status_code in expected_status


#  Тест получения остатков по статусу.
def test_inventories_by_status(order_store_pet_fixture):
    response_status_code = order_store_pet_fixture.get_inventories_by_status()
    assert response_status_code[1] == 200


# Тест удаления заказа.
def test_delete_order(test_data, pet_store_pet_fixture, order_store_pet_fixture):
    pet_test_data = test_data.generate_test_data()
    pet_store_pet_fixture.add_new_pet_store(test_data=pet_test_data, status="approved")
    order_store_pet_fixture.create_order_for_pet(test_data=pet_test_data, status="approved")
    order_delete = order_store_pet_fixture.order_delete(orderId=pet_test_data.order_data.id)
    assert order_delete["code"] == 200
