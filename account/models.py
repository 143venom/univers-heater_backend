from django.db import models
from django.contrib.auth.models import AbstractUser
from random import randint
from django.utils import timezone
from .managers import CustomUserManager


# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Email", max_length=255)
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone_number", "address"]
    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.username:
            username_base = self.email.split("@")[0]
            username = username_base
            counter = 1
            while CustomUser.objects.filter(username=username).exists():
                username = f"{username_base}{counter}"
                counter += 1
            self.username = username
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name
