import uuid

import factory

from core.apps.crm.domain.entities import LeadStatus, PriorityStatus
from core.apps.crm.models.lead import Lead


class LeadFactory(factory.django.DjangoModelFactory):
    id = factory.LazyAttribute(lambda s: uuid.uuid4().hex)
    company = factory.Faker("pystr")
    contact_person = factory.Faker("pystr")
    email = factory.Faker("email")
    phone = factory.Faker("pyint", min_value=9000000000, max_value=9999999999)
    estimated_value = factory.Faker("pyint")
    website = factory.Faker("url")
    status = LeadStatus.NEW
    priority = PriorityStatus.LOW

    class Meta:
        model = Lead
