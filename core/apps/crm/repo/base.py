from abc import ABC, abstractmethod
from uuid import UUID

from core.apps.crm.domain.entities import LeadEntity


class AbstractLeadRepository(ABC):
    @abstractmethod
    def save(self, lead: LeadEntity):
        ...

    @abstractmethod
    def get(self, lead_id: UUID):
        ...

    @abstractmethod
    def update(self, lead: LeadEntity):
        ...

    @abstractmethod
    def delete(self, lead_id: UUID):
        ...
