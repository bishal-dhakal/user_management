from django.contrib.auth.models import AbstractUser, Group
from django.db import models

from .constants import ROLE_CHOICES, ROLE_DOCTOR
from .UserManager import CustomUserManager


class User(AbstractUser):
    # Role field using the string-based ROLE_CHOICES
    groups = models.ForeignKey(Group, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, blank=True, null=True)
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


class Patient(models.Model):
    name = models.CharField(max_length=30)
    doctor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="patients",
        limit_choices_to={"role": ROLE_DOCTOR},
    )

    def __str__(self):
        return self.name
