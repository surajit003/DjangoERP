from typing import Optional, Sequence
from uuid import UUID

from django.db import IntegrityError

from core.apps.crm.domain.entities import LeadEntity
from core.apps.crm.models.lead import Lead
from core.apps.crm.repo.base import AbstractLeadRepository
from core.apps.crm.repo.exceptions import LeadExistException, LeadDoesNotExistException


class LeadRepository(AbstractLeadRepository):
    @staticmethod
    def _get_instance(instance_id):
        return Lead.objects.filter(id=instance_id).first()

    def _create_or_update_instance(self, instance):
        if self._get_instance(instance.id):
            Lead.objects.filter(id=instance.id).update(**instance.dict())
            lead = self._get_instance(instance.id)
        else:
            lead = Lead.objects.create(**instance.dict())

        return LeadEntity(**lead.__dict__)

    def save(self, obj: LeadEntity) -> LeadEntity:
        try:
            return self._create_or_update_instance(obj)
        except IntegrityError:
            raise LeadExistException

    def get(self, lead_id: UUID) -> LeadEntity:
        if lead := self._get_instance(lead_id):
            return LeadEntity(**lead.__dict__)
        else:
            raise LeadDoesNotExistException

    def delete(self, lead_id: UUID) -> None:
        instance = self._get_instance(lead_id)
        return instance.delete()

    def get_all(self) -> Optional[Sequence[LeadEntity]]:
        leads = Lead.objects.all()
        return [LeadEntity(**lead.__dict__) for lead in leads]
