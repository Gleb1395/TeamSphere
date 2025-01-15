from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class Worker(AbstractUser):
    position = models.ForeignKey("Position", on_delete=models.CASCADE, related_name="workers")
    objects = UserManager()


class Position(models.Model):
    name = models.CharField(max_length=120)
