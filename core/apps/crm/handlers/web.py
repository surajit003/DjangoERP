from pydantic import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.apps.crm.domain.exceptions import InvalidPhoneNumberException
from core.apps.crm.handlers.factories import InternalUseCaseFactory
from core.apps.crm.logic.lead import create_lead, get_lead, update_lead, get_leads
from core.apps.crm.repo.exceptions import LeadExistException, LeadDoesNotExistException


class LeadAPIView(APIView):
    def post(self, request):
        data = request.data
        try:
            lead = create_lead(
                lead_data=data, lead_repo=InternalUseCaseFactory().get_repo()
            )
        except LeadExistException:
            return Response(
                {"message": "Lead with that Email Exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except InvalidPhoneNumberException:
            return Response(
                {
                    "message": "Invalid Phone Number",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except ValidationError as exc:
            return Response(
                {
                    "message": exc.errors(),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(lead.dict(), status=status.HTTP_201_CREATED)

    def get(self, request, lead_id=None):
        if not lead_id:
            leads_dict = {}
            if leads := get_leads(lead_repo=InternalUseCaseFactory().get_repo()):
                leads_dict = [lead.__dict__ for lead in leads]

            return Response(
                {
                    "message": leads_dict,
                },
                status=status.HTTP_200_OK,
            )
        try:
            lead = get_lead(
                lead_id=lead_id, lead_repo=InternalUseCaseFactory().get_repo()
            )
        except LeadDoesNotExistException:
            return Response(
                {"message": "Lead with that Email Doesnot exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(lead.dict(), status=status.HTTP_200_OK)

    def put(self, request, lead_id):
        try:
            data = request.data
            lead = get_lead(
                lead_id=lead_id, lead_repo=InternalUseCaseFactory().get_repo()
            )
        except LeadDoesNotExistException:
            return Response(
                {"message": "Lead with that Email Doesnot exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        lead = update_lead(
            lead_entity=lead,
            lead_data=data,
            lead_repo=InternalUseCaseFactory().get_repo(),
        )
        return Response(lead.dict(), status=status.HTTP_200_OK)
