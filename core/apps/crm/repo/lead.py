from typing import Optional

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

    def update(self, obj: LeadEntity) -> Optional[LeadEntity]:
        is_update = Lead.objects.filter(id=obj.id).update(**obj.dict())
        if is_update:
            lead_obj = Lead.objects.get(id=obj.id)
            return LeadEntity(**lead_obj.__dict__)
        else:
            return None

    def delete(self, lead_id) -> None:
        Lead.objects.filter(id=lead_id).delete()

    def get(self, lead_id) -> LeadEntity:
        lead_obj = Lead.objects.get(id=lead_id)
        return LeadEntity(lead_obj.__dict__)
