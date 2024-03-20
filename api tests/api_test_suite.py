from framework.api_page.petstore_method import PetStoreUser
from conftest import user_test_data

pet_shop_fixture = PetStoreUser()


def test_create_user(user_test_data):
    test_data = user_test_data.user_test_data()
    user = pet_shop_fixture.create_user(user_test_data=test_data, password="12345")
    assert user["code"] == 200


def test_create_user_with_array(user_test_data):
    test_data_1 = user_test_data.user_test_data()
    test_data_2 = user_test_data.user_test_data()
    user_array = pet_shop_fixture.create_user_with_array(user_test_data_1=test_data_1, user_test_data_2=test_data_2,
                                                         password="12345")
    assert user_array["code"] == 200


def test_create_user_with_list(user_test_data):
    test_data = user_test_data.user_test_data()
    user_array = pet_shop_fixture.create_user_with_list(user_test_data=test_data, password="12345")
    assert user_array["code"] == 200


def test_get_user_name(user_test_data):
    test_data = user_test_data.user_test_data()
    pet_shop_fixture.create_user(user_test_data=test_data, password="12345")
    user_name = pet_shop_fixture.get_user_name(user_name=test_data["username"])
    assert user_name["username"] == test_data["username"]


def test_put_user_name(user_test_data):
    test_data = user_test_data.user_test_data()
    new_user_name = user_test_data.user_test_data()
    pet_shop_fixture.create_user(user_test_data=test_data, password="12345")
    new_username = pet_shop_fixture.put_user_name(user_name=new_user_name["username"], user_test_data=test_data,
                                                  password="12345")
    assert new_username["code"] == 200


def test_user_delete(user_test_data):
    test_data = user_test_data.user_test_data()
    pet_shop_fixture.create_user(user_test_data=test_data, password="12345")
    user = pet_shop_fixture.user_delete(user_name=test_data["username"])
    assert user["code"] == 200
