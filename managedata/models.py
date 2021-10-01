import os

from django.db import models
from django.utils import timezone

class DataInfo(models.Model):
    data_file = models.FileField(upload_to='data/')
    upload_at = models.DateTimeField(default=timezone.now)
    
    def delete(self, *args, **kwargs):
        self.data_file.delete()
        super().delete(*args, **kwargs)
    
    def __str__(self):
        return os.path.basename(self.data_file.file.name)
# Create your models here.
