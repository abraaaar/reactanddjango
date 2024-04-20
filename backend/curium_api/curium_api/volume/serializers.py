from rest_framework import serializers
from .models import VolumeRecord
from curium_api.user.models import User
from curium_api.organization.models import Organization
from .models import Status

class CreateVolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolumeRecord
        fields = [
            "patient_id",
            "study_id",
            "volume_meta",
            "report_meta",
            "isAutomated",
        ]

    def save(self):
        user = User.objects.get(id=self.context["request"].user.id)
        org = Organization.objects.get(org_name="Org1")
        status = Status.UPLOADED
        patient_id = self.validated_data["patient_id"]
        study_id = self.validated_data["study_id"]
        volume_meta = self.validated_data.get("volume_meta", None)
        report_meta = self.validated_data.get("report_meta", None)
        is_automated = self.validated_data.get("isAutomated", False)
        volume = VolumeRecord(
            uploaded_by=user,
            org=org,
            status=status,
            patient_id=patient_id,
            study_id=study_id,
            volume_meta=volume_meta,
            report_meta=report_meta,
            isAutomated=is_automated,
        )
        volume.save()
        return volume


class UpdateVolumeSerialization(serializers.ModelSerializer):

    class Meta:
        model = VolumeRecord
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.uploaded_by = validated_data.get("uploaded_by", instance.uploaded_by)
        instance.org = validated_data.get("org", instance.org)
        instance.status = validated_data.get("status", instance.status)
        instance.patient_id = validated_data.get("patient_id", instance.patient_id)
        instance.study_id = validated_data.get("study_id", instance.study_id)
        instance.volume_meta = validated_data.get("volume_meta", instance.volume_meta)
        instance.report_meta = validated_data.get("report_meta", instance.report_meta)
        instance.isAutomated = validated_data.get("isAutomated", instance.isAutomated)
        instance.save()
        return instance

class VolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolumeRecord
        fields = "__all__"
