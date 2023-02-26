from abc import abstractmethod, ABC

from core.apps.crm.repo.base import AbstractLeadRepository
from core.apps.crm.repo.lead import LeadRepository


class AbstractUseCaseFactory(ABC):
    @abstractmethod
    def get_repo(self) -> AbstractLeadRepository:
        ...


class InternalUseCaseFactory(AbstractUseCaseFactory):
    """
    Use this factory when you want to save the data in DjangoERP
    """

    def get_repo(self) -> LeadRepository:
        return LeadRepository()
