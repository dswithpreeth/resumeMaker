from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length= 100)
    email = models.CharField(max_length= 100)
    degree = models.CharField(max_length= 100)
    skills = models.CharField(max_length= 100)

    