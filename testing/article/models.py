from uuid import uuid4

from django.conf import settings
from django.db import models

# Create your models here.
class Article(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4,editable=False)
    title = models.CharField(max_length=191)
    content = models.TextField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='%(class)s_created_by'
    )
    created_at = models.DateTimeField(auto_now_add=True)