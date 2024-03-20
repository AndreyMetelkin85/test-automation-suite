import pytest
from test_data.test_data import TestData


@pytest.fixture
def user_test_data():
    return TestData()
