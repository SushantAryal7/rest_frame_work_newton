from django.db import models
import uuid
from uuid import uuid4

import os

# Create your models here.

class Folder(models.Model):
    uid         = models.UUIDField(primary_key=True , editable= False, default=uuid.uuid4)
    created_at  = models.DateField(auto_now= True)

def get_upload_file(instance , filename):
    return os.path.join(str(instance.folder.uid), filename)

class Files(models.Model):
    folder      = models.ForeignKey(Folder , on_delete=models.CASCADE )
    file        = models.FileField(upload_to='')
    created_at  = models.DateField(auto_now= True)