import uuid

import factory

from core.apps.common.datetime import utc_datetime
from core.apps.crm.domain.entities import LeadStatus, PriorityStatus
from core.apps.crm.models.lead import Lead


class LeadFactory(factory.django.DjangoModelFactory):
    id = factory.LazyAttribute(lambda s: uuid.uuid4().hex)
    company = factory.Faker("pystr")
    contact_person = factory.Faker("pystr")
    email = factory.Faker("email")
    phone = "+9551370038"
    estimated_value = factory.Faker("pyint")
    website = factory.Faker("url")
    status = LeadStatus.NEW
    priority = PriorityStatus.LOW
    created = factory.LazyFunction(utc_datetime)
    modified = factory.LazyFunction(utc_datetime)

    class Meta:
        model = Lead
