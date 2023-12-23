from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    age = models.PositiveSmallIntegerField(null=True)
    weight = models.PositiveSmallIntegerField(null=True)
