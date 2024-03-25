from datetime import datetime, timezone
from faker import Faker
import random


class TestData:
    """
        Класс для создания тестовых данных.
    """

    def __init__(self):
        """
            Инициализирует объект класса TestData с экземпляром класса Faker для генерации
            тестовых данных на английском языке.
        """
        self.faker = Faker("en_US")

    def user_test_data(self):
        """Генерирует данные для одного пользователя."""

        user = {
            "id": random.randint(1, 9999),
            "username": self.faker.user_name(),
            "firstName": self.faker.first_name(),
            "lastName": self.faker.last_name(),
            "email": self.faker.email(),
            "password": self.faker.password(),
            "phone": self.faker.phone_number(),
            "userStatus": random.randint(1, 10)
        }
        return user

    def pet_test_data(self):
        """
            Генерирует данные для животного.
        """
        pet = {
            "id": random.randint(1, 9999),
            "category": {
                "id": random.randint(1, 9999),
                "name": self.faker.word()
            },
            "name": self.faker.word(),
            "photoUrls": [
                self.faker.image_url()
            ],
            "tags": [
                {
                    "id": random.randint(1, 9999),
                    "name": self.faker.word()
                }
            ],

        }
        return pet

    def order_test_data(self):
        """
            Генерирует тестовые данные для заказа.
        """
        current_datetime = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
        order = {
            "id": random.randint(1, 9999),
            "quantity": random.randint(1, 10),
            "shipDate": current_datetime,
        }
        return order
