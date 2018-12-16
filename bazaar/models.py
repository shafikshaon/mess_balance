from django.db import models

from accounts.models import User
from core.models.TimeLog import TimeLog


class Bazaar(TimeLog):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bazaar_user')
    bazaar_date = models.DateField(blank=False, null=False)
    item_name = models.CharField(max_length=255, null=False, blank=False)
    item_weight = models.FloatField(null=True, blank=True)
    item_price = models.FloatField(null=False, blank=False)

    class Meta:
        app_label = "bazaar"
        db_table = "bazaar"
        verbose_name = "bazaar"
        verbose_name_plural = "bazaar"
