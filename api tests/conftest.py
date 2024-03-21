import pytest

from framework.api_page.petstore_method import PetStoreUser
from test_data.test_data import TestData


@pytest.fixture
def user_test_data():
    """
        Фикстура для предоставления тестовых данных.
    """
    return TestData()


@pytest.fixture
def pet_store_user_fixture():
    """
         Фикстура для предоставления методов для взаимодействия с API магазина домашних животных.
    """
    return PetStoreUser()
