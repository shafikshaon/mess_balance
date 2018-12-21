import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, F
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.edit import FormMixin

from accounts.models import User
from bazaar.models import Bazaar
from extra_cost.models import ExtraCost
from meals.models import Meal


class ReckoningView(LoginRequiredMixin, FormMixin, View):
    template_name = 'core/reckoning.html'
    login_url = 'accounts/login/'

    def get(self, request, *args, **kwargs):
        today = datetime.datetime.now().day
        current_month = datetime.datetime.now().month
        total_active_user = User.objects.filter(is_active=True).count()
        previous_month = datetime.date.today().replace(day=1) - datetime.timedelta(days=1)
        month_meals_count = Meal.objects \
            .filter(meal_date__month=current_month) \
            .aggregate(total_meals=Sum(F('breakfast') + F('lunch') + F('dinner')))
        month_total_bazaar = Bazaar.objects \
            .filter(bazaar_date__month=current_month) \
            .aggregate(total_bazaar=Sum('item_price'))
        month_total_extra_cost = ExtraCost.objects \
            .filter(expense_date__month=current_month) \
            .aggregate(total_extra_costs=Sum('cost'))

        meal_rate = month_total_bazaar['total_bazaar'] / month_meals_count['total_meals']
        extra_cost_per_member = month_total_extra_cost['total_extra_costs'] / total_active_user

        month_user_meals = Meal.objects.select_related('user') \
            .filter(meal_date__month=current_month) \
            .values('user_id', 'user__first_name', 'user__last_name') \
            .annotate(total_meals=Sum(F('breakfast') + F('lunch') + F('dinner')))
        month_user_bazaar = Bazaar.objects.select_related('user') \
            .filter(bazaar_date__month=current_month) \
            .values('user_id', 'user__first_name', 'user__last_name') \
            .annotate(total_bazaar=Sum('item_price'))
        month_user_extra_cost = ExtraCost.objects.select_related('user') \
            .filter(expense_date__month=current_month) \
            .values('user_id', 'user__first_name', 'user__last_name') \
            .annotate(total_extra_costs=Sum('cost'))

        month_user_bazaar2 = User.objects \
            .select_related('meals') \
            .values('user_id', 'user__first_name', 'user__last_name') \
            .prefetch_related('user__bazaar_user') \
            .values('user__bazaar_user__item_price') \
            .aggregate(h=Sum('user__bazaar_user__item_price'))

        # .annotate(total_bazaar=Sum('user__bazaar_user__item_price'), total_meals=Sum(F('breakfast') + F('lunch') +
        #                                                                             F('dinner')))
        # month_user_bazaar = Bazaar.objects.select_related('user') \
        #     .filter(bazaar_date__month=current_month) \
        #     .values('user_id', 'user__first_name', 'user__last_name') \
        #     .annotate(total_bazaar=Sum('item_price'))
        print(month_user_bazaar2)

        context = {
            'month_meals_count': month_meals_count,
            'month_total_bazaar': month_total_bazaar,
            'month_total_extra_cost': month_total_extra_cost,
            'meal_rate': meal_rate,
            'extra_cost_per_member': extra_cost_per_member,
            'month_user_meals': month_user_meals,
            'month_user_bazaar': month_user_bazaar,
            'month_user_extra_cost': month_user_extra_cost,
        }
        return render(request, self.template_name, context)
