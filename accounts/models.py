from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(blank=True, max_length=30)

    def __str__(self):
        return self.username
