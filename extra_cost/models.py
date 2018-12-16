from django.db import models

from accounts.models import User
from core.models.TimeLog import TimeLog


class ExtraCost(TimeLog):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='extra_cost_user')
    expense_date = models.DateField(blank=False, null=False)
    cost_name = models.CharField(max_length=255, null=False, blank=False)
    cost = models.FloatField(null=False, blank=False)

    class Meta:
        app_label = "extra_cost"
        db_table = "extra_costs"
        verbose_name = "extra_cost"
        verbose_name_plural = "extra_costs"
