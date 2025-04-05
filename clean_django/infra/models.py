from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseUserModel(AbstractUser):
    objects = UserManager()

    class Meta:
        abstract = True
