from core.apps.crm.repo.base import AbstractLeadRepository
from core.apps.crm.repo.lead import LeadRepository


class AbstractUseCaseFactory:

    def get_repo(self):
        ...


class InternalUseCaseFactory(AbstractUseCaseFactory):

    def get_repo(self):
        return LeadRepository()


