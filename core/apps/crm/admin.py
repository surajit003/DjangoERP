from django.contrib import admin

# Register your models here.
from core.apps.crm.models.lead import Lead


@admin.register(Lead)
class LeadAdminForm(admin.ModelAdmin):
    list_display = (
        "company",
        "contact_person",
        "status",
        "priority",
    )
    list_filter = (
        "id",
        "company",
        "status",
    )
    non_editable_fields = (
        "updated",
        "created",
    )
