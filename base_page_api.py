import requests


class BaseAPI:
    """
        Базовый класс для взаимодействия с API.
    """
    def __init__(self):
        """
            Инициализирует объект класса BaseAPI с базовым URL API.
        """
        self.base_url = 'https://petstore.swagger.io'

    def get(self, endpoint):
        """
            Выполняет GET-запрос к API по-указанному endpoint.
        """
        try:
            response = requests.get(self.base_url + endpoint)
            response.raise_for_status()
            return response.json(), response.status_code
        except requests.exceptions.HTTPError as err:
            print(f"HTTP Error: {err}")
            return None, response.status_code

    def post(self, endpoint, data, headers=None, files=None):
        """
            Выполняет POST-запрос к API по-указанному endpoint с передачей данных.
        """
        try:
            response = requests.post(self.base_url + endpoint, json=data, headers=headers, files=files)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP Error: {err}")
            return None

    def put(self, endpoint, data):
        """
            Выполняет PUT-запрос к API по-указанному endpoint с передачей данных.
        """
        try:
            response = requests.put(self.base_url + endpoint, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP Error: {err}")
            return None

    def delete(self, endpoint):
        """
            Выполняет DELETE-запрос к API по-указанному endpoint.
        """
        try:
            response = requests.delete(self.base_url + endpoint)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP Error: {err}")
            return None
