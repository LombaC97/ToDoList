from django.db import models
from django.conf import settings

# Create your models here.

class Folder(models.Model):
    folder_id = models.AutoField(primary_key = True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.PROTECT)
    name = models.CharField(max_length = 30)

class Activity(models.Model):
    activity_id = models.AutoField(primary_key = True)
    folder_id = models.ForeignKey(Folder, on_delete = models.CASCADE)
    name = models.CharField(max_length = 30)

