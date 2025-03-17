from datetime import datetime, timezone
import faker
import random
from dataclasses import dataclass

from qa_test_data.default_user_data import User, Category, Tags, PetData, OrderData, TextBoxFormData, \
    RegistrationFormData, StudentRegistrationData


@dataclass
class TestData:
    __test__ = False
    user: User
    category: Category
    tags: Tags
    pet_data: PetData
    order_data: OrderData
    text_box_form_data: TextBoxFormData
    # registration_form_data: RegistrationFormData
    # student_registration_form_data: StudentRegistrationData


class DataGenerator:
    """ Класс для создания тестовых данных. """

    def __init__(self):
        """
            Инициализирует объект класса TestData с экземпляром класса Faker для генерации
            тестовых данных на английском языке.
        """
        self.faker = faker.Faker(locale="en_US")
        # self.user = User()
        # self.category = Category()
        # self.tags = Tags()
        # self.pet_data = PetData()
        # self.order_data = OrderData()
        # self.box_form_data = TextBoxFormData()
        # self.registration_form_data = RegistrationFormData()
        # self.student_registration_form_data = StudentRegistrationData()

    def create_user_data(self):
        """Генерирует данные для одного пользователя."""

        id = random.randint(1, 9999)
        username = self.faker.user_name()
        first_name = self.faker.first_name()
        last_name = self.faker.last_name()
        email = self.faker.email(domain="google.com")
        password = self.faker.password()
        phone = self.faker.numerify("+1 (###) ###-####")
        user_status = random.randint(1, 10)

        user = User()
        user.id = id
        user.username = username
        user.firstName = first_name
        user.lastName = last_name
        user.email = email
        user.password = password
        user.phone = phone
        user.userStatus = user_status

        return user

    def create_pet_data(self):
        """ Генерирует данные для животного. """

        id = random.randint(1, 9999)
        name = self.faker.word()
        photo_urls = self.faker.image_url()

        pet_data = PetData()
        pet_data.id = id
        pet_data.name = name
        pet_data.photoUrls = photo_urls

        return pet_data

    def create_tags_data(self):
        id = random.randint(1, 9999)
        name = self.faker.word()

        tags = Tags()
        tags.id = id
        tags.name = name

        return tags

    def create_category_data(self):
        id = random.randint(1, 9999)
        name = self.faker.word()

        category = Category()
        category.id = id
        category.name = name

        return category

    def create_order_test_data(self):
        """ Генерирует тестовые данные для заказа. """

        current_datetime = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
        id = random.randint(1, 9999)
        quantity = random.randint(1, 10)
        ship_date = current_datetime

        order_data = OrderData()
        order_data.id = id
        order_data.quantity = quantity
        order_data.shipDate = ship_date

        return order_data

    def db_test_data(self):
        """
            Генерирует тестовые данные для использования в тестах базы данных.
        """
        db_data = {
            "first_name": self.faker.first_name(),
            "last_name": self.faker.last_name(),
            "department": self.faker.job(),
            "position": self.faker.job(),
            "phone": self.faker.phone_number(),
            "email": self.faker.email()
        }
        return db_data

    def create_text_box_form_data(self):
        """ Генерирует тестовые данные для использования в тестах, связанных с заполнением формы. """

        fullname = self.faker.name()
        email = self.faker.email(domain="google.com")
        current_address = self.faker.address()
        permanent_address = self.faker.address()

        box_form_data = TextBoxFormData()
        box_form_data.fullname = fullname
        box_form_data.email = email
        box_form_data.current_address = current_address
        box_form_data.permanent_address = permanent_address

        return box_form_data

    def registration_form_data(self):
        """
           Генерирует тестовые данные для использования в тестах регистрации.
        """
        registration_form = {
            "first_name": self.faker.first_name(),
            "last_name": self.faker.last_name(),
            "email": self.faker.email(),
            "age": random.randint(18, 60),
            "salary": random.randint(1000, 5000),
            "department": self.faker.job()

        }
        return registration_form

    def student_registration_form(self):
        student_form = {
            "first_name": self.faker.first_name(),
            "last_name": self.faker.last_name(),
            "email": self.faker.email(),
            "mobile_number": ''.join(random.choices('0123456789', k=10)),
            "current_address": self.faker.address(),

        }
        return student_form

    def generate_test_data(self):
        user = self.create_user_data()
        pet_data = self.create_pet_data()
        tags = self.create_tags_data()
        category = self.create_category_data()
        order_data = self.create_order_test_data()
        box_form_data = self.create_text_box_form_data()
        return TestData(user=user,
                        pet_data=pet_data,
                        category=category,
                        tags=tags,
                        order_data=order_data,
                        text_box_form_data=box_form_data
                        )
