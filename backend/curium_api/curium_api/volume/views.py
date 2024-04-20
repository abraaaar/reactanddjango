from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    CreateVolumeSerializer,
    VolumeSerializer,
    UpdateVolumeSerialization,
)
from .models import VolumeRecord

@api_view(["POST", "GET"])
@permission_classes([IsAuthenticated])
def volume_view(request):
    context = {"request": request}
    if request.method == "POST":
        serializer = CreateVolumeSerializer(data=request.data, context=context)
        data = {}
        if serializer.is_valid():
            volume = serializer.save()
            data["record_id"] = volume.record_id
            data["upload_date"] = volume.upload_date
            data["volume_meta"] = volume.volume_meta
            data["report_meta"] = volume.report_meta
            data["patient_id"] = volume.patient_id
            data["study_id"] = volume.study_id
            data["isAutomated"] = volume.isAutomated
            data["status"] = volume.status
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        volumes = VolumeRecord.objects.filter(uploaded_by=request.user.id)
        serializer = VolumeSerializer(volumes, many=True)
        return Response(serializer.data)

@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def volume_record_view(request, pk):
    try:
        volume = VolumeRecord.objects.get(record_id=pk)
    except VolumeRecord.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = VolumeSerializer(volume)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = UpdateVolumeSerialization(volume, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        volume.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
