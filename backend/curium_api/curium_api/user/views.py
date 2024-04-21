from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from curium_api.user.serializers import RegistrationSerializer, ProfileSerializer
from curium_api.membership.serializers import MembershipSerializer
from curium_api.membership.models import Membership


@api_view(["POST"])
@permission_classes([AllowAny])
def registration_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()

            data["email"] = user.email_id
            data["lname"] = user.lname
            data["fname"] = user.fname
            data["id"] = user.id
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    query = request.GET.get("membership", False)

    if query == "true":

        membership = Membership.objects.filter(user=request.user.id)
        membership_serializer = MembershipSerializer(membership, many=True)

        profile_serializer = ProfileSerializer(user, many=False)
        data = profile_serializer.data
        data["membership"] = membership_serializer.data
        return Response(data, status=status.HTTP_200_OK)

    serializer = ProfileSerializer(user, many=False)
    return Response(serializer.data)
