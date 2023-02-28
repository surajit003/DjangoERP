import pytest
from pytest_factoryboy import register

from .factories import LeadFactory
from ..repo.lead import LeadRepository

register(LeadFactory, name="lead_factory")


@pytest.fixture
def lead_repo():
    return LeadRepository()
