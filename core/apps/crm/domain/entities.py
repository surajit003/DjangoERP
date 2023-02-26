from enum import Enum

from pydantic import EmailStr, AnyHttpUrl

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
