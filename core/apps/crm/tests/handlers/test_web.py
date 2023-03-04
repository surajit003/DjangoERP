import pytest

pytestmark = pytest.mark.django_db


def test_customer_create(client):
    response = client.post(
        "/api/v1/leads/",
        data={
            "company": "test company",
            "contact_person": "test user",
            "email": "abc@example.com",
            "phone": "+2547839920201",
            "estimated_value": 100,
        },
        content_type="application/json",
    )
    resp_json = response.json()
    assert response.status_code == 201
    assert resp_json["company"] == "test company"
    assert resp_json["contact_person"] == "test user"
    assert resp_json["email"] == "abc@example.com"
    assert resp_json["phone"] == "+2547839920201"


def test_customer_create_raises_lead_exist_exception(client, lead_factory):
    lead_factory(email="abc@example.com")
    response = client.post(
        "/api/v1/leads/",
        data={
            "company": "test company",
            "contact_person": "test uer",
            "email": "abc@example.com",
            "phone": "+2547839920201",
            "estimated_value": 100,
        },
        content_type="application/json",
    )
    resp_json = response.json()
    assert response.status_code == 400
    assert resp_json["message"] == "Lead with that Email Exist"


def test_customer_create_raises_invalid_phone_number_exception(client):
    response = client.post(
        "/api/v1/leads/",
        data={
            "company": "test company",
            "contact_person": "test uer",
            "email": "abc@example.com",
            "phone": "+254783992",
            "estimated_value": 100,
        },
        content_type="application/json",
    )
    resp_json = response.json()
    assert response.status_code == 400
    assert resp_json["message"] == "Invalid Phone Number"


def test_customer_create_raises_validation_error(client):
    response = client.post(
        "/api/v1/leads/",
        data={
            "company": "test company",
            "contact_person": "test uer",
            "email": "abc@example.com",
            "estimated_value": 100,
        },
        content_type="application/json",
    )
    resp_json = response.json()
    assert response.status_code == 400
    assert resp_json["message"][0]["loc"] == ["phone"]
    assert resp_json["message"][0]["msg"] == "field required"
