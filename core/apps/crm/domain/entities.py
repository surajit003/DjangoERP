import re
from enum import Enum

from pydantic import EmailStr, AnyHttpUrl, validator

from core.apps.common.entities import Entity


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
    website: AnyHttpUrl
    confidence: int
    estimated_value: int
    status: LeadStatus
    priority: PriorityStatus

    @validator("phone")
    def phone_validation(cls, v):
        # For reference - https://stackoverflow.com/questions/70414211/pydantic-custom-data-type-for-phone-number
        # -value-error-missing
        regex = r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$"
        if v and not re.search(regex, v, re.I):
            raise ValueError("Invalid Phone Number.")
        return v
