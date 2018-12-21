import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, F
from django.shortcuts import render
from django.views.generic.base import View

from bazaar.models import Bazaar
from extra_cost.models import ExtraCost
from meals.models import Meal


class DashboardView(LoginRequiredMixin, View):
    template_name = 'core/dashboard.html'
    login_url = 'accounts/login/'

    def get(self, request, *args, **kwargs):
        today = datetime.datetime.now().day
        current_month = datetime.datetime.now().month
        previous_month = datetime.date.today().replace(day=1) - datetime.timedelta(days=1)
        today_meals_count = Meal.objects \
            .filter(meal_date__day=today) \
            .aggregate(today_breakfast_count=Sum('breakfast'), today_lunch_count=Sum('lunch'),
                       today_dinner_count=Sum('dinner'))

        today_meals = Meal.objects.select_related('user').filter(meal_date__day=today)

        current_month_total_meals = Meal.objects.filter(meal_date__month=current_month) \
            .aggregate(total_meals=Sum(F('breakfast') + F('lunch') + F('dinner')))
        current_month_total_bazaar = Bazaar.objects.filter(bazaar_date__month=current_month) \
            .aggregate(total_bazaar=Sum('item_price'))
        current_month_total_extra_cost = ExtraCost.objects.filter(expense_date__month=current_month) \
            .aggregate(total_extra_costs=Sum('cost'))

        previous_month_total_meals = Meal.objects.filter(meal_date__month=previous_month.month) \
            .aggregate(total_meals=Sum(F('breakfast') + F('lunch') + F('dinner')))
        previous_month_total_bazaar = Bazaar.objects.filter(bazaar_date__month=previous_month.month) \
            .aggregate(total_bazaar=Sum('item_price'))
        previous_month_total_extra_cost = ExtraCost.objects.filter(expense_date__month=previous_month.month) \
            .aggregate(total_extra_costs=Sum('cost'))

        current_month_user_meals = Meal.objects.select_related('user') \
            .filter(meal_date__month=current_month) \
            .values('user_id', 'user__first_name', 'user__last_name') \
            .annotate(total_meals=Sum(F('breakfast') + F('lunch') + F('dinner')))
        current_month_user_bazaar = Bazaar.objects.select_related('user') \
            .filter(bazaar_date__month=current_month) \
            .values('user_id', 'user__first_name', 'user__last_name') \
            .annotate(total_bazaar=Sum('item_price'))
        current_month_user_extra_cost = ExtraCost.objects.select_related('user') \
            .filter(expense_date__month=current_month) \
            .values('user_id', 'user__first_name', 'user__last_name') \
            .annotate(total_extra_costs=Sum('cost'))

        previous_month_user_meals = Meal.objects.select_related('user') \
            .filter(meal_date__month=previous_month.month) \
            .values('user_id', 'user__first_name', 'user__last_name') \
            .annotate(total_meals=Sum(F('breakfast') + F('lunch') + F('dinner')))
        previous_month_user_bazaar = Bazaar.objects.select_related('user') \
            .filter(bazaar_date__month=previous_month.month) \
            .values('user_id', 'user__first_name', 'user__last_name') \
            .annotate(total_bazaar=Sum('item_price'))
        previous_month_user_extra_cost = ExtraCost.objects.select_related('user') \
            .filter(expense_date__month=previous_month.month) \
            .values('user_id', 'user__first_name', 'user__last_name') \
            .annotate(total_extra_costs=Sum('cost'))

        context = {
            'today_meals_count': today_meals_count,
            'today_meals': today_meals,
            'current_month_total_meals': current_month_total_meals,
            'current_month_user_meals': current_month_user_meals,
            'current_month_total_bazaar': current_month_total_bazaar,
            'current_month_user_bazaar': current_month_user_bazaar,
            'current_month_total_extra_cost': current_month_total_extra_cost,
            'current_month_user_extra_cost': current_month_user_extra_cost,
            'previous_month_total_meals': previous_month_total_meals,
            'previous_month_total_bazaar': previous_month_total_bazaar,
            'previous_month_total_extra_cost': previous_month_total_extra_cost,
            'previous_month_user_meals': previous_month_user_meals,
            'previous_month_user_bazaar': previous_month_user_bazaar,
            'previous_month_user_extra_cost': previous_month_user_extra_cost,
            'previous_month': previous_month
        }
        return render(request, self.template_name, context)
