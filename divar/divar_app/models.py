from django.db import models
from django.contrib.auth.models import User
class Advertisment(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    




# Create your models here.
