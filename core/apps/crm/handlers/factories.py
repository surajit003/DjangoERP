from abc import abstractmethod, ABC

from core.apps.crm.repo.base import AbstractLeadRepository
from core.apps.crm.repo.lead import LeadRepository


class AbstractUseCaseFactory(ABC):
    @abstractmethod
    def get_repo(self):
        ...


class InternalUseCaseFactory(AbstractUseCaseFactory):
    def get_repo(self):
        return LeadRepository()
