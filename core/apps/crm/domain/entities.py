import re
from enum import Enum
from typing import Optional

from pydantic import EmailStr, AnyHttpUrl, validator

from core.apps.common.entities import Entity
from core.apps.crm.domain.exceptions import InvalidPhoneNumberException


class LeadStatus(str, Enum):
    NEW = "new"
    CONTACTED = "contacted"
    IN_PROGRESS = "inprogress"
    LOST = "lost"
    WON = "won"


class PriorityStatus(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Lead(Entity):
    company: str
    contact_person: str
    email: EmailStr
    phone: str
    website: Optional[AnyHttpUrl]
    estimated_value: int
    status: LeadStatus = LeadStatus.NEW
    priority: PriorityStatus = PriorityStatus.LOW

    @validator("phone")
    def phone_validation(cls, v):
        # For reference - https://stackoverflow.com/questions/70414211/pydantic-custom-data-type-for-phone-number
        # -value-error-missing
        regex = r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$"
        if v and not re.search(regex, v, re.I):
            raise InvalidPhoneNumberException("Invalid Phone Number.")
        return v
