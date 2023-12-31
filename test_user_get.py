import requests
from lib.api_helper import ApiHelper


class TestUserGet(ApiHelper):
    def test_get_user_details_not_found(self):
        response = requests.get('https://playground.learnqa.ru/api/user/2')

        ApiHelper.assert_json_has_key(response, "username")
        ApiHelper.assert_json_has_not_key(response, "email")
        ApiHelper.assert_json_has_not_key(response, "firstname")
        ApiHelper.assert_json_has_not_key(response, "lastname")

    def test_get_user_details_auth_as_same_user(self):
        data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_headers(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id_from_auth_method}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid})

        expected_fields = ["username", "email", "firstName", "lastName"]
        ApiHelper.assert_json_has_keys(response2, expected_fields)
