import json

from conftest import api_client


def test_get_companies(api_client):
    response = api_client.send_get_request(endpoint="api/companies/",
                                           params={"status": None,
                                                   "limit": 1,
                                                   "offset": 0})
    assert response.status_code == 200
    companies_data = response.json()
    print("Response data:")
    print(json.dumps(companies_data, indent=4))


