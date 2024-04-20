from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import MembershipSerializer, CreateMembershipSerializer
from .models import Membership

@api_view(["POST", "GET"])
@permission_classes([IsAuthenticated])
def membership_view(request):
    if request.method == "POST":
        serializer = CreateMembershipSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            membership = serializer.save()
            data["org_id"] = str(membership.org.org_id)
            data["user_id"] = str(membership.user.id)
            data["role"] = membership.role
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        membership = Membership.objects.filter(user=request.user)
        serializer = MembershipSerializer(membership, many=True)
        return Response(serializer.data)
