from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from core.apps.crm.domain.entities import LeadEntity


class AbstractLeadRepository(ABC):
    @abstractmethod
    def save(self, lead: LeadEntity) -> Optional[LeadEntity]:
        ...

    @abstractmethod
    def get(self, lead_id: UUID) -> Optional[LeadEntity]:
        ...

    @abstractmethod
    def update(self, lead: LeadEntity) -> LeadEntity:
        ...

    @abstractmethod
    def delete(self, lead_id: UUID) -> None:
        ...
