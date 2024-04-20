from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegistrationSerializer, ProfileSerializer
from curium_api.membership.models import Membership

@api_view(["POST"])
@permission_classes([AllowAny])
def registration_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data["response"] = "successfully registered new user."
            data["email"] = user.email_id
            data["lname"] = user.lname
            data["fname"] = user.fname
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    serializer = ProfileSerializer(user, many=False)
    membership = Membership.objects.get(user=user)
    return Response({
        **serializer.data,
        "role": membership.role
    })
