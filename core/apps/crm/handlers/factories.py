from core.apps.crm.repo.base import AbstractLeadRepository
from core.apps.crm.repo.lead import LeadRepository


def get_repository_for_lead_creation(use_case_type: str) -> AbstractLeadRepository:
    if use_case_type == "internal":
        return LeadRepository()
