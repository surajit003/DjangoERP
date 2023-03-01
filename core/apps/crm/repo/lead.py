from typing import Optional
from uuid import UUID

from django.db import IntegrityError

from core.apps.crm.domain.entities import LeadEntity
from core.apps.crm.models.lead import Lead
from core.apps.crm.repo.base import AbstractLeadRepository
from core.apps.crm.repo.exceptions import LeadExistException


class LeadRepository(AbstractLeadRepository):
    @staticmethod
    def _get_instance(instance_id):
        return Lead.objects.filter(id=instance_id).first()

    def _create_or_update_instance(self, instance):
        if self._get_instance(instance.id):
            Lead.objects.filter(id=instance.id).update(**instance.dict())
            return self._get_instance(instance.id)
        else:
            return Lead.objects.create(**instance.dict())

    def save(self, obj: LeadEntity) -> LeadEntity:
        try:
            return self._create_or_update_instance(obj)
        except IntegrityError as exc:
            raise LeadExistException(exc) from exc

    def get(self, lead_id: UUID) -> LeadEntity:
        return self._get_instance(lead_id)

    def delete(self, lead_id: UUID):
        instance = self._get_instance(lead_id)
        return instance.delete()
