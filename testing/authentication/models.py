from uuid import uuid4

from django.db import models
from django.db.models import UUIDField


# Create your models here.
class verifyEmail(models.Model):
    uuid = UUIDField(primary_key=True,default=uuid4,editable=False)
    is_verified = models.BooleanField(default=False)
    email = models.EmailField(unique=True)