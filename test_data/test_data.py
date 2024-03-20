from faker import Faker
import random


class TestData:
    def __init__(self):
        self.faker = Faker("en_US")

    def user_test_data(self):

        """Генерирует данные для одного пользователя."""

        user = {
            "id": random.randint(1, 100),
            "username": self.faker.user_name(),
            "firstName": self.faker.first_name(),
            "lastName": self.faker.last_name(),
            "email": self.faker.email(),
            "password": self.faker.password(),
            "phone": self.faker.phone_number(),
            "userStatus": random.randint(1, 10)
        }
        return user
