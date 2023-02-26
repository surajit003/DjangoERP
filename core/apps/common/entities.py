import uuid
from datetime import datetime

from pydantic import BaseModel, Field

from core.apps.common.datetime import utc_datetime


class Entity(BaseModel):
    id: uuid.UUID = Field(default_factory=lambda: uuid.uuid4().hex)
    created_at: datetime = Field(default_factory=utc_datetime)
    updated_at: datetime = Field(default_factory=utc_datetime)
