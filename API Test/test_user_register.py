import random
import string

import requests
import pytest

from lib.api_helper import ApiHelper
from datetime import datetime


class TestUserRegistry(ApiHelper):
    def setup(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"
        self.username = f""

    def test_create_user_successfully(self):
        data = {
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'password': '123',
            'email': self.email
        }

        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        ApiHelper.assert_code_status(response, 200)
        ApiHelper.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = {
            'password': '123',
            'email': email,
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa'
        }
        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        ApiHelper.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    def test_registration_without_at_symbol_should_fail(self):
        invalid_email = self.email.replace("@", "")
        data = {
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'password': '123',
            'email': invalid_email
        }

        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        ApiHelper.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "Invalid email format"

    @pytest.mark.parametrize("invalid_email", ["@example.com", "example@"])
    def test_registration_with_invalid_email(self, invalid_email):
        local_part_invalid_email = self.email.split("@")[0] + invalid_email
        data = {
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'password': '123',
            'email': f"{local_part_invalid_email}@example.com"
        }

        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        ApiHelper.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "Invalid email format"

    @pytest.mark.parametrize('username', ['a', 'A', 1])
    def test_create_user_with_single_char_name(self, username):
        data = {
            'username': username,
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'password': '123',
            'email': self.email
        }

        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)
        ApiHelper.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "The value of 'username' field is too short"

    def test_create_user_with_long_and_complex_username(self):
        data = {
            'username': ''.join(random.choice(string.ascii_letters) for _ in range(300)),
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'password': '123',
            'email': self.email
        }

        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        ApiHelper.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "The value of 'username' field is too long"
