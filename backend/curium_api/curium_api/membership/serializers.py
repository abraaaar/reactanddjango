from rest_framework import serializers
from .models import Membership
from curium_api.user.models import User
from curium_api.organization.models import Organization

class CreateMembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Membership
        fields = ["user", "role"]

    def save(self):
        user = User.objects.get(id=self.validated_data["user"].id)
        org = Organization.objects.get(org_name="Org1")
        membership = Membership(
            user=user,
            org=org,
            role=self.validated_data["role"],
        )
        membership.save()
        return membership

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = "__all__"
