from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import CreateOrganizationSerializer, OrganizationSerializer
from curium_api.membership.serializers import CreateMembershipSerializer
from .models import Organization
from curium_api.membership.models import Role


@api_view(["POST", "GET"])
@permission_classes([IsAuthenticated])
def organization_view(request):
    context = {"request": request}

    if request.method == "POST":
        serializer = CreateOrganizationSerializer(data=request.data, context=context)
        data = {}
        if serializer.is_valid():
            organization = serializer.save()

            data["owner"] = request.user.id
            data["name"] = organization.org_name
            data["address"] = organization.org_address
            data["description"] = organization.org_description
            data["id"] = organization.org_id

            membership_obj = {
                "user": str(request.user.id),
                "org": str(organization.org_id),
                "role": Role.ADMIN,
            }

            membership_serializer = CreateMembershipSerializer(data=membership_obj)
            if membership_serializer.is_valid():
                _ = membership_serializer.save()

            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":

        organizations = Organization.objects.filter(org_owner_id=request.user.id)
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(serializer.data)
