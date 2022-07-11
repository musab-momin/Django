from django.db import models
from django.utils import timezone
import uuid
import os


# Create your models here.
class Folder(models.Model):
    folder_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


def get_upload_path(instance, filname):
    return os.path.join(str(instance.folder.folder_id), filename)


class File(models.Model):
    file = models.FileField(upload_to=get_upload_path)
    created_at = models.DateTimeField(default=timezone.now)
    folder = models.ForeignKey(Folder, on_delete = models.CASCADE)
    

    def __str__(self):
        return self.folder.folder_id
    

