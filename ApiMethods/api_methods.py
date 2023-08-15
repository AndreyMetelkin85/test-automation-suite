from api_base_page import BaseApi
import requests


class ApiMethods(BaseApi):

    def get_companies(self, status="ACTIVE", limit=10, offset=0):
        url = f"{self.base_url}/api/companies/"
        params = {"status": status,
                  "limit": limit,
                  "offset": offset}

        response = requests.get(url, params=params)
        return response

    def get_companies_id(self, company_id: int):
        url = f"{self.base_url}/api/companies/{company_id}"
        params = {"company_id": company_id}

        response = requests.get(url, params=params)
        return response

