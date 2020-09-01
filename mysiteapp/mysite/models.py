from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Business(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=12)
    rating = models.IntegerField
