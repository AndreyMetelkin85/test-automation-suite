import json

import pytest

from conftest import api_client


@pytest.mark.parametrize("status, limit, offset", [("ACTIVE", 3, 0),
                                                   ("BANKRUPT", 2, 0),
                                                   ("CLOSED", 2, 0),
                                                   ("INVALID_STATUS", 2, 0),
                                                   ("ACTIVE", 1, 1),
                                                   ("ACTIVE", 1, 2),
                                                   ("CLOSED", 1, 1),
                                                   ("BANKRUPT", 1, 1)])
def test_get_companies(api_client, status, limit, offset):
    response = api_client.send_get_request(endpoint="api/companies/",
                                           params={"status": status,
                                                   "limit": limit,
                                                   "offset": offset})
    if status == "INVALID_STATUS":
        assert response.status_code == 422  # Ошибка согласно требованиям
        return

    assert response.status_code == 200
    companies_data = response.json()

    expected_companies = []

    if status == "ACTIVE" and limit == 1 and offset == 1:
        expected_companies = [
            {"company_id": 2, "company_name": "Google", "company_status": "ACTIVE"}
        ]

    elif status == "ACTIVE" and limit == 1 and offset == 2:
        expected_companies = [
            {"company_id": 3, "company_name": "Toyota", "company_status": "ACTIVE"}
        ]

    elif status == "CLOSED" and limit == 1 and offset == 1:
        expected_companies = [
            {"company_id": 6, "company_name": "BitcoinCorp", "company_status": "CLOSED"}
        ]

    elif status == "BANKRUPT" and limit == 1 and offset == 1:
        expected_companies = [
            {"company_id": 7, "company_name": "Xiaomi", "company_status": "BANKRUPT"}
        ]

    elif status == "ACTIVE":
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


@pytest.mark.parametrize("company_id, expected_status", [
    (-1, 404),
    (0, 404),
    (1, 200),
    (2, 200),
    (3, 200),
    (7, 200),
    (8, 404)
])
def test_get_companies_id(api_client, company_id, expected_status):
    response = api_client.send_get_request(endpoint=f"api/companies/{company_id}")

    assert response.status_code == expected_status

    if expected_status == 200:
        companies_data = response.json()
    else:
        companies_data = response.json()

        if company_id == 1:
            expected_company = {
                "company_id": 1,
                "company_name": "Tesla",
                "company_address": "Nicholastown, IL 80126",
                "company_status": "ACTIVE"
            }
        elif company_id == 2:
            expected_company = {
                "company_id": 2,
                "company_name": "Google",
                "company_address": "1093 Cooke Harbor Apt. 908",
                "company_status": "ACTIVE"
            }
        elif company_id == 3:
            expected_company = {
                "company_id": 3,
                "company_name": "Toyota",
                "company_address": "Davidberg, MN 88952",
                "company_status": "ACTIVE"
            }
        elif company_id == 7:
            expected_company = {
                "company_id": 7,
                "company_name": "Xiaomi",
                "company_address": "Port Valeriefurt, HI 15914",
                "company_status": "BANKRUPT"
            }
        else:
            expected_company = None

        if expected_company:
            assert companies_data["company_id"] == expected_company["company_id"]
            assert companies_data["company_name"] == expected_company["company_name"]
            assert companies_data["company_address"] == expected_company["company_address"]
            assert companies_data["company_status"] == expected_company["company_status"]

    print("Response data:")
    print(json.dumps(companies_data, indent=4))


# Test Accept-Language header
def test_accept_language_header(api_client):
    headers = {"Accept-Language": "en"}
    response = api_client.send_get_request(endpoint="api/companies/", headers=headers)
    assert response.status_code == 200

    companies_data = response.json()
    assert "meta" in companies_data
    assert "data" in companies_data
    assert len(companies_data["data"]) > 0

    print("Response data:")
    print(json.dumps(companies_data, indent=4))


@pytest.mark.parametrize("limit, offset", [(0, 1)])
def test_get_users_limit(api_client, limit, offset):
    response = api_client.send_get_request(endpoint="api/users/",
                                           params={"limit": limit,
                                                   "offset": offset})
    assert response.status_code == 200
    print(json.dumps(response.json(), indent=4))
