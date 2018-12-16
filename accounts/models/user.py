from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from core.models.TimeLog import TimeLog


class CustomUserManager(UserManager):

    def create_admin_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser, TimeLog):
    user = models.ForeignKey('self', on_delete=models.CASCADE, related_name='accounts_user')
    email = models.EmailField(blank=False, null=False)
    is_admin = models.BooleanField(default=False, null=False, blank=False)
    member_from = models.DateField(blank=False, null=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    objects = CustomUserManager()

    class Meta:
        app_label = "accounts"
        db_table = "users"
        verbose_name = "user"
        verbose_name_plural = "users"
