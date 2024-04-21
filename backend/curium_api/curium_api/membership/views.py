from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    MembershipSerializer,
    CreateMembershipSerializer,
    UpdateMembershipSerialization,
)
from .models import Membership


@api_view(["POST", "GET"])
@permission_classes([IsAuthenticated])
def membership_view(request):

    if request.method == "POST":
        serializer = CreateMembershipSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            membership = serializer.save()

            data["org_id"] = membership.org.org_id
            data["user_id"] = membership.user.id
            data["role"] = membership.role
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":

        membership = Membership.objects.filter(user=request.user.id)
        serializer = MembershipSerializer(membership, many=True)
        return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def membership_view_path_id(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        membership = Membership.objects.get(membership_id=pk)
    except Membership.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = MembershipSerializer(membership)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = UpdateMembershipSerialization(membership, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        membership.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
