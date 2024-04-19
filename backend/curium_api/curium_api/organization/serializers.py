from rest_framework import serializers
from .models import Organization
from curium_api.user.models import User


class CreateOrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ["org_name", "org_description", "org_address"]

    def save(self):
        user = User.objects.get(id=self.context["request"].user.id)
        organization = Organization(
            org_owner=user,
            org_name=self.validated_data["org_name"],
            org_description=self.validated_data["org_description"],
            org_address=self.validated_data["org_address"],
        )
        organization.save()
        return organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"
