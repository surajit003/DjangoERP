from core.apps.crm.domain.entities import LeadEntity
from core.apps.crm.models.lead import Lead
from core.apps.crm.repo.base import AbstractLeadRepository


class LeadRepository(AbstractLeadRepository):
    def save(self, obj: LeadEntity):
        lead_obj = Lead(**obj.dict())
        return lead_obj.save()

    def update(self, obj: LeadEntity):
        pass

    def delete(self, lead_id):
        pass

    def get(self, lead_id):
        pass
