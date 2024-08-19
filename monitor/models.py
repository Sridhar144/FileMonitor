from django.db import models

# Create your models here.
# monitor/models.py


class MonitoredFile(models.Model):
    file_path = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
