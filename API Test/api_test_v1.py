import json

import pytest

from conftest import api_client


@pytest.mark.parametrize("status, limit, offset", [("ACTIVE", 3, 0), ("BANKRUPT", 2, 0), ("CLOSED", 2, 0)])
def test_get_companies(api_client, status, limit, offset):
    response = api_client.send_get_request(endpoint="api/companies/",
                                           params={"status": status,
                                                   "limit": limit,
                                                   "offset": offset})
    assert response.status_code == 200
    companies_data = response.json()

    expected_companies = []

    if status == "ACTIVE":
        expected_companies = [
            {"company_id": 1, "company_name": "Tesla", "company_status": "ACTIVE"},
            {"company_id": 2, "company_name": "Google", "company_status": "ACTIVE"},
            {"company_id": 3, "company_name": "Toyota", "company_status": "ACTIVE"}
        ]
    elif status == "BANKRUPT":
        expected_companies = [
            {"company_id": 4, "company_name": "Nord", "company_status": "BANKRUPT"},
            {"company_id": 7, "company_name": "Xiaomi", "company_status": "BANKRUPT"}
        ]
    elif status == "CLOSED":
        expected_companies = [
            {"company_id": 5, "company_name": "Apple", "company_status": "CLOSED"},
            {"company_id": 6, "company_name": "BitcoinCorp", "company_status": "CLOSED"}
        ]

    for expected_company in expected_companies:
        found_company = None
        for company in companies_data["data"]:
            if company["company_id"] == expected_company["company_id"]:
                found_company = company
                break

        assert found_company is not None, f"Company with ID {expected_company['company_id']} not found in response"
        assert found_company["company_name"] == expected_company["company_name"], \
            f"Expected company name: {expected_company['company_name']}, but got: {found_company['company_name']}"
        assert found_company["company_status"] == expected_company["company_status"], \
            f"Expected company status: {expected_company['company_status']}, but got: {found_company['company_status']}"

    print("Response data:")
    print(json.dumps(companies_data, indent=4))


@pytest.mark.parametrize("company_id, expected_status", [(-1, 404), (0, 404), (1, 200), (7, 200), (8, 404)])
def test_get_companies_id(api_client, company_id, expected_status):
    response = api_client.send_get_request(endpoint=f"api/companies/{company_id}")

    assert response.status_code == expected_status
    companies_data = response.json()
    print("Response data:")
    print(json.dumps(companies_data, indent=4))
