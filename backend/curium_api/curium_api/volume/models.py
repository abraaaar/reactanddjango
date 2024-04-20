from django.db import models
import uuid
from curium_api.user.models import User
from curium_api.organization.models import Organization

class Status(models.TextChoices):
    UPLOADED = "UPLOADED", "Uploaded"
    QUEUED = "QUEUED", "Queued"
    PROCESSING = "PROCESSING", "Processing"
    INTERMEDIATE_STATE = "INTERMEDIATE_STATE", "Intermediate State"
    COMPLETED = "COMPLETED", "Completed"

class VolumeRecord(models.Model):
    record_id = models.UUIDField(
        primary_key=True, auto_created=True, default=uuid.uuid4, editable=False
    )
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=Status.choices, blank=False, null=False
    )
    patient_id = models.CharField(max_length=255, blank=False)
    study_id = models.CharField(max_length=255, blank=False)
    volume_meta = models.JSONField(null=True, blank=True)
    report_meta = models.JSONField(null=True, blank=True)
    isAutomated = models.BooleanField(default=False)
