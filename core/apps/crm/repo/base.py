from abc import ABC, abstractmethod
from uuid import UUID

from core.apps.crm.domain.entities import Lead


class AbstractLeadRepository(ABC):
    @abstractmethod
    def save(self, lead: Lead):
        ...

    @abstractmethod
    def get(self, lead_id: UUID):
        ...

    @abstractmethod
    def update(self, lead: Lead):
        ...

    @abstractmethod
    def delete(self, lead_id: UUID):
        ...
