import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render
from django.views.generic.base import View

from meals.models import Meal


class DashboardView(LoginRequiredMixin, View):
    template_name = 'core/dashboard.html'
    login_url = 'accounts/login/'

    def get(self, request, *args, **kwargs):
        today = datetime.datetime.now().day
        today_meals_count = Meal.objects \
            .filter(meal_date__day=today) \
            .aggregate(today_breakfast_count=Sum('breakfast')*2, today_lunch_count=Sum('lunch'),
                       today_dinner_count=Sum('dinner'))

        today_meals = Meal.objects.select_related('user').filter(meal_date__day=today)

        context = {
            'today_meals_count': today_meals_count,
            'today_meals': today_meals
            # 'today_breakfast_count': today_breakfast_count,
            # 'today_lunch_count': today_lunch_count,
            # 'today_dinner_count': today_dinner_count
        }
        return render(request, self.template_name, context)
