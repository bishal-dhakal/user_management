from django.contrib.auth.models import AbstractUser
from django.db import models

from .constants import ROLE_CHOICES
from .UserManager import CustomUserManager


# Create your models here.
class User(AbstractUser):
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    objects = CustomUserManager()


class Patient(models.Model):
    name = models.CharField(max_length=30)
