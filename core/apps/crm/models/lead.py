from django.db import models
from simple_history.models import HistoricalRecords

from core.apps.common.models import TimeStampedModel


class Lead(TimeStampedModel):
    NEW = "new"
    CONTACTED = "contacted"
    IN_PROGRESS = "inprogress"
    LOST = "lost"
    WON = "won"

    CHOICES_STATUS = (
        (NEW, "New"),
        (CONTACTED, "Contacted"),
        (IN_PROGRESS, "In progress"),
        (LOST, "Lost"),
        (WON, "Won"),
    )

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

    CHOICES_PRIORITY = (
        (LOW, "Low"),
        (MEDIUM, "Medium"),
        (HIGH, "High"),
    )

    company = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField(unique=True, db_index=True)
    phone = models.CharField(max_length=255, db_index=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    estimated_value = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=25, choices=CHOICES_STATUS, default=NEW)
    priority = models.CharField(max_length=25, choices=CHOICES_PRIORITY)

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.company} {self.email} {self.phone}"

    class Meta:
        ordering = ("created",)
