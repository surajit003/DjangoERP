import pytest

from core.apps.crm.logic.lead import create_lead, list_all

pytestmark = pytest.mark.django_db


def test_create_lead(lead_factory, lead_repo):
    lead_data = lead_factory.build()
    lead_data_dict = lead_data.__dict__
    lead = create_lead(lead_data_dict, lead_repo)
    assert lead
    assert lead.company == lead_data_dict["company"]
    assert lead.contact_person == lead_data_dict["contact_person"]


def test_update_lead(lead_factory, lead_repo):
    lead_data = lead_factory.build()
    lead_data_dict = lead_data.__dict__
    lead = create_lead(lead_data_dict, lead_repo)
    assert lead
    assert lead.company == lead_data_dict["company"]
    assert lead.contact_person == lead_data_dict["contact_person"]


def test_list_all(lead_factory, lead_repo):
    lead_factory()
    lead_factory()
    leads = list_all(lead_repo)
    assert leads
    assert len(leads) == 2
