from core.apps.crm.models.lead import Lead
from core.apps.crm.repo.base import AbstractLeadRepository


class LeadRepository(AbstractLeadRepository):
    def save(self, obj):
        lead_dict = obj.dict()
        lead_obj = Lead(lead_dict)
        return lead_obj.save()

    def update(self, obj):
        pass

    def delete(self, lead_id):
        pass

    def get(self, lead_id):
        pass
