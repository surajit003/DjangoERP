from typing import Optional, Sequence
from uuid import UUID

from core.apps.crm.domain.entities import LeadEntity
from core.apps.crm.repo.base import AbstractLeadRepository


def create_lead(lead_data: dict, lead_repo: AbstractLeadRepository) -> LeadEntity:
    lead_entity = LeadEntity(**lead_data)
    return lead_repo.save(lead_entity)


def update_lead(
    lead_entity: LeadEntity, lead_data: dict, lead_repo: AbstractLeadRepository
) -> LeadEntity:
    lead_entity.__dict__.update(lead_data)
    return lead_repo.save(lead_entity)


def get_lead(lead_id: UUID, lead_repo: AbstractLeadRepository) -> Optional[LeadEntity]:
    return lead_repo.get(lead_id)


def get_leads(lead_repo: AbstractLeadRepository) -> Optional[Sequence[LeadEntity]]:
    return lead_repo.get_all()
