from rest_framework import serializers
from .models import Organization
from curium_api.user.models import User
from curium_api.membership.models import Membership


class CreateMembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Membership
        fields = ["user", "org", "role"]

    def save(self):

        user = User.objects.get(id=self.validated_data["user"].id)
        org = Organization.objects.get(org_id=self.validated_data["org"].org_id)
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
