import requests
from lib.api_helper import ApiHelper


class TestUserRegistry(ApiHelper):

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

        assert response.status_code == 400, f"Unexpected status code: {response.status_code}"
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"
