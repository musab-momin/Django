from django.db import models
from django.utils import timezone


# Create your models here.
class ApiNote(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    content  = models.TextField(null=False, blank=False)


    def __str__(self):
        return self.content[:10]
    