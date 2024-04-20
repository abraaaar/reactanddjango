from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, email_id, fname, lname, password=None):
        if not email_id:
            raise ValueError("Users must have an email address")

        user = self.model(
            email_id=self.normalize_email(email_id),
            fname=fname,
            lname=lname,
            username=email_id,  # Set the username to the email_id
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    id = models.UUIDField(
        primary_key=True, auto_created=True, default=uuid.uuid4, editable=False
    )
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email_id = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email_id"]

    objects = MyAccountManager()

    def __str__(self):
        return self.email_id

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True
