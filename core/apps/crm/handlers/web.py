from pydantic import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.apps.crm.domain.exceptions import InvalidPhoneNumberException
from core.apps.crm.handlers.factories import InternalUseCaseFactory
from core.apps.crm.logic.lead import create_lead
from core.apps.crm.repo.exceptions import LeadExistException


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
