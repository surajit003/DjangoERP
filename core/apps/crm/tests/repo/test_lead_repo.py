import pytest

from core.apps.crm.domain.entities import LeadEntity
from core.apps.crm.repo.exceptions import LeadExistException

pytestmark = pytest.mark.django_db


def test_lead_repository_create(lead_factory, lead_repo):
    lead_data = lead_factory.build()
    lead_entity = LeadEntity(**lead_data.__dict__)
    lead_repo.save(lead_entity)
    lead_obj = lead_repo.get(lead_entity.id)
    assert lead_obj.id == lead_entity.id


def test_lead_repository_raises_exception(lead_factory, lead_repo):
    lead_data_1 = lead_factory.build(email="abc@example.com")
    lead_data_2 = lead_factory.build(email="abc@example.com")

    lead_entity_1 = LeadEntity(**lead_data_1.__dict__)
    lead_entity_2 = LeadEntity(**lead_data_2.__dict__)

    lead_repo.save(lead_entity_1)
    with pytest.raises(LeadExistException) as exc:
        lead_repo.save(lead_entity_2)

    assert isinstance(exc, LeadExistException)

    breakpoint()


def test_lead_repository_get(lead_factory, lead_repo):
    lead_data = lead_factory()
    lead_entity = lead_repo.get(lead_data.id)
    assert lead_entity


def test_lead_repository_update(lead_factory, lead_repo):
    lead_data_updated = lead_factory()
    lead_data_updated.company = "test-company-1"
    lead_data_updated.contact_person = "test-user-1"
    lead_data_updated_entity = LeadEntity(**lead_data_updated.__dict__)
    lead_repo.save(lead_data_updated_entity)
    lead = lead_repo.get(lead_data_updated.id)
    assert lead.company == "test-company-1"
    assert lead_data_updated.contact_person == "test-user-1"
