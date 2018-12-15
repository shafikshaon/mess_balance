from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from core.models.TimeLog import TimeLog


class CustomUserManager(UserManager):

    def create_admin_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_user', False)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, password, **extra_fields)

    def create_website_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_user', True)
        extra_fields.setdefault('is_admin', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser, TimeLog):
    email = models.EmailField(blank=False, null=False)
    is_user = models.BooleanField(default=False, null=False, blank=False)
    is_admin = models.BooleanField(default=False, null=False, blank=False)

    objects = CustomUserManager()

    class Meta:
        app_label = "accounts"
        db_table = "users"
        verbose_name = "user"
        verbose_name_plural = "users"
