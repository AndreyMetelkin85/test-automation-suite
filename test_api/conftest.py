import pytest

from framework.api_page.petstore_user_method import PetStoreUser
from framework.api_page.petstore_pet_method import PetStorePet
from framework.api_page.petstore_order_method import PetStoreOrder
from test_data.test_data import TestData


@pytest.fixture
def user_test_data():
    """
        Фикстура для предоставления тестовых данных.
    """
    return TestData()


@pytest.fixture
def pet_test_data():
    """
        Фикстура для предоставления тестовых данных.
    """
    return TestData()


@pytest.fixture
def order_test_data():
    """
        Фикстура для предоставления тестовых данных для заказа.
    """
    return TestData()


@pytest.fixture
def pet_store_user_fixture():
    """
         Фикстура для предоставления методов для взаимодействия с API магазина домашних животных.
    """
    return PetStoreUser()


@pytest.fixture
def pet_store_pet_fixture():
    """
        Фикстура для предоставления методов для взаимодействия с API магазина домашних животных.
    """
    return PetStorePet()


@pytest.fixture
def order_store_pet_fixture():
    """
        Фикстура для создания экземпляра класса PetStoreOrder для тестирования операций заказа.
    """

    return PetStoreOrder()
