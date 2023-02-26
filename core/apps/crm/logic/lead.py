from core.apps.crm.domain.entities import LeadEntity
from core.apps.crm.repo.base import AbstractLeadRepository


def create_lead(lead_data: dict, lead_repo: AbstractLeadRepository) -> LeadEntity:
    lead_entity = LeadEntity(**lead_data)
    lead = lead_repo.save(lead_entity)
    return lead
