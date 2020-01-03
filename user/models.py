from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    username = models.TextField()
    password = models.CharField(max_length = 30)
    confirm = models.CharField(max_length = 30)