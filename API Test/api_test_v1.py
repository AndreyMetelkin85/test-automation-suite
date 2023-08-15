import json

import pytest

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


@pytest.mark.parametrize("company_id, expected_status", [(-1, 404), (0, 404), (1, 200), (7, 200), (8, 404)])
def test_get_companies_id(api_client, company_id, expected_status):
    response = api_client.send_get_request(endpoint=f"api/companies/{company_id}")

    assert response.status_code == expected_status
    companies_data = response.json()
    print("Response data:")
    print(json.dumps(companies_data, indent=4))
