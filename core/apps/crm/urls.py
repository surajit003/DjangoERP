from django.urls import path

from core.apps.crm.handlers.web import LeadAPIView

app_name = "Lead"

urlpatterns = [
    path("leads/", LeadAPIView.as_view(), name="leads"),
    path("leads/<uuid:lead_id>/", LeadAPIView.as_view(), name="lead"),
]
