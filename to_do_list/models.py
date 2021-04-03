from django.db import models
from django.conf import settings

# Create your models here.

#Model folder which is associated with an user and has a name
class Folder(models.Model):
    folder_id = models.AutoField(primary_key = True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.PROTECT)
    name = models.CharField(max_length = 30)

#Model acitvity which is associated with a folder and has a name
class Activity(models.Model):
    activity_id = models.AutoField(primary_key = True)
    folder_id = models.ForeignKey(Folder, on_delete = models.CASCADE)
    name = models.CharField(max_length = 30)

