from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User():
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

