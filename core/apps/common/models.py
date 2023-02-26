from django.db import models
from django.utils import timezone


class TimeStampedModel(models.Model):
    id = models.CharField(max_length=180, primary_key=True)
    created = models.DateTimeField(default=timezone.now, editable=False, db_index=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
