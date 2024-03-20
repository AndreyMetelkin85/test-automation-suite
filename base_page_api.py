import requests


class BaseAPI:
    def __init__(self):
        self.base_url = 'https://petstore.swagger.io'

    def get(self, endpoint):
        try:
            response = requests.get(self.base_url + endpoint)
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP Error: {err}")
            return None

    def post(self, endpoint, data):
        try:
            response = requests.post(self.base_url + endpoint, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP Error: {err}")
            return None

    def put(self, endpoint, data):
        try:
            response = requests.put(self.base_url + endpoint, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP Error: {err}")
            return None

    def delete(self, endpoint):
        try:
            response = requests.delete(self.base_url + endpoint)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP Error: {err}")
            return None
