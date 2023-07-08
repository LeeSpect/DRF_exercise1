from django.db import models
from django.contrib.auth.models import AbstractUser

class Members(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username