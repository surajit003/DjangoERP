import json

import pytest

from core.apps.crm.domain.entities import LeadEntity

pytestmark = pytest.mark.django_db


def test_lead_create(client):
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


def test_lead_create_raises_lead_exist_exception(client, lead_factory):
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


def test_lead_create_raises_invalid_phone_number_exception(client):
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


def test_lead_create_raises_validation_error(client):
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


def test_get_lead(client, lead_factory):
    lead = lead_factory()
    response = client.get(
        f"/api/v1/leads/{lead.id}/",
    )
    resp_json = response.json()
    assert response.status_code == 200
    assert resp_json
    assert resp_json["company"] == lead.company
    assert resp_json["id"] == str(lead.id)


def test_get_lead_raises_lead_does_not_exist_error(client):
    response = client.get(
        "/api/v1/leads/1082cef2-de55-4683-b78c-79e6b5ef8f6b/",
    )
    resp_json = response.json()
    assert response.status_code == 400
    assert resp_json["message"] == "Lead with that Email Doesnot exist"


def test_lead_update(client, lead_factory):
    lead = lead_factory(company="test_company", contact_person="test_user")
    lead_entity = LeadEntity(**lead.__dict__)
    lead_entity.company = "test_company_1"
    lead_entity.contact_person = "test_user_1"
    response = client.put(
        f"/api/v1/leads/{lead.id}/",
        data=lead_entity.__dict__,
        content_type="application/json",
    )
    resp_json = response.json()
    assert response.status_code == 200
    assert resp_json["company"] == "test_company_1"
    assert resp_json["contact_person"] == "test_user_1"


def test_lead_update_raises_lead_does_not_exist_exception(client, lead_factory):
    lead = lead_factory(company="test_company", contact_person="test_user")
    lead_entity = LeadEntity(**lead.__dict__)
    lead_entity.company = "test_company_1"
    lead_entity.contact_person = "test_user_1"
    response = client.put(
        "/api/v1/leads/1082cef2-de55-4683-b78c-79e6b5ef8f6c/",
        data=lead_entity.__dict__,
        content_type="application/json",
    )
    resp_json = response.json()
    assert response.status_code == 400
    assert resp_json["message"] == "Lead with that Email Doesnot exist"
