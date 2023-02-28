import uuid

import pytest

from core.apps.crm.models.lead import Lead

pytestmark = pytest.mark.django_db


def test_lead_create():
    lead_id = uuid.uuid4().hex
    lead = Lead.objects.create(
        id=lead_id,
        company="test company",
        contact_person="test user",
        email="abc@example.com",
        phone="999999999",
        estimated_value=100,
    )
    assert lead.id == lead_id
    assert str(lead) == f"{lead.company} {lead.email} {lead.phone}"
