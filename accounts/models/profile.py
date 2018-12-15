from django.db import models
from accounts.models.user import User
from core.models.TimeLog import TimeLog


class Profile(TimeLog):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        app_label = "accounts"
        db_table = "profiles"
        verbose_name = "profiles"
