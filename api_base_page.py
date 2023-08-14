import requests


class BaseApi:

    def __init__(self, base_url):
        self.base_url = base_url

    def send_get_request(self, endpoint, params=None, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=params, headers=headers)
        return response

    def send_post_request(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data, headers=headers)
        return response

    def send_put_request(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.put(url, json=data, headers=headers)
        return response

    def send_delete_request(self, endpoint, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.delete(url, headers=headers)
        return response
