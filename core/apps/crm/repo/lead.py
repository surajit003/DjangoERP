from core.apps.crm.repo.base import AbstractLeadRepository


class LeadRepository(AbstractLeadRepository):

    def save(self, lead):
        return Lead.objects.create()