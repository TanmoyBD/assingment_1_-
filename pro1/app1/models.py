
from django.db import models

class YourTask(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    is_completed = models.IntegerField(default=0)
