from typing import Optional
from uuid import UUID

from django.db import IntegrityError

from core.apps.crm.domain.entities import LeadEntity
from core.apps.crm.models.lead import Lead
from core.apps.crm.repo.base import AbstractLeadRepository
from core.apps.crm.repo.exceptions import LeadExistException


class LeadRepository(AbstractLeadRepository):
    def save(self, obj: LeadEntity) -> Optional[LeadEntity]:
        try:
            lead_obj = Lead(**obj.dict())
            lead_obj.save()
            return obj
        except IntegrityError as exc:
            raise LeadExistException(exc)

    def update(self, lead_id: UUID, obj: LeadEntity) -> LeadEntity:
        Lead.objects.filter(id=lead_id).update(**obj.dict())
        lead_obj = Lead.objects.get(id=lead_id)
        return LeadEntity(**lead_obj.__dict__)

    def delete(self, lead_id: UUID) -> None:
        Lead.objects.filter(id=lead_id).delete()

    def get(self, lead_id: UUID) -> LeadEntity:
        lead_obj = Lead.objects.get(id=lead_id)
        return LeadEntity(**lead_obj.__dict__)
