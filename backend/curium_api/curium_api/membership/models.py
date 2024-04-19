from django.db import models
import uuid
import uuid
from curium_api.user.models import User
from curium_api.organization.models import Organization


class Role(models.TextChoices):
    ADMIN = "ADMIN", "Admin"
    SURGEON = "SURGEON", "Surgeon"
    TELERADIOLOGIST = "TELERADIOLOGIST", "Teleradiologist"


class Membership(models.Model):
    membership_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20, choices=Role.choices, null=False, blank=False
    )
