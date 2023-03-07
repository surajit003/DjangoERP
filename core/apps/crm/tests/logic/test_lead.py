import pytest

from core.apps.crm.logic.lead import create_lead, get_leads, update_lead

pytestmark = pytest.mark.django_db


def test_create_lead(lead_factory, lead_repo):
    lead_data = lead_factory.build()
    lead_data_dict = lead_data.__dict__
    lead = create_lead(lead_data_dict, lead_repo)
    assert lead
    assert lead.company == lead_data_dict["company"]
    assert lead.contact_person == lead_data_dict["contact_person"]


def test_update_lead(lead_factory, lead_repo):
    lead_data = lead_factory(company="test company", contact_person="test-user")
    lead = lead_repo.get(lead_data.id)
    updated_lead = lead.copy()
    updated_lead.company = "test updated company"
    updated_lead.contact_person = "test user 1"
    update_lead(lead, updated_lead.__dict__, lead_repo)

    lead = lead_repo.get(lead_data.id)
    assert lead.company == "test updated company"
    assert lead.contact_person == "test user 1"


def test_list_all(lead_factory, lead_repo):
    lead_factory()
    lead_factory()
    leads = get_leads(lead_repo)
    assert leads
    assert len(leads) == 2
