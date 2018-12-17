import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView

from meals.forms import AddMealForm, UpdateMealForm
from meals.models import Meal


class MealCreateView(LoginRequiredMixin, CreateView):
    template_name = 'meals/add.html'
    form_class = AddMealForm
    login_url = '/accounts/login/'

    def form_valid(self, form):
        is_added_meal = Meal.objects.filter(meal_date__day=datetime.datetime.today().day, user_id=self.request.user.pk)
        meal = form.save(commit=False)
        meal.user_id = self.request.user.pk
        meal.save()
        messages.success(self.request, 'Meal added successfully.')
        return HttpResponseRedirect(reverse('meal-add'))

    def dispatch(self, *args, **kwargs):
        is_added_meal = Meal.objects.filter(meal_date__day=datetime.datetime.today().day, user_id=self.request.user.pk)
        if is_added_meal:
            messages.error(self.request, 'Today meals already added.')
            return HttpResponseRedirect(reverse('meal-list'))

        return super().dispatch(*args, **kwargs)


class MealListView(LoginRequiredMixin, ListView):
    template_name = 'meals/list.html'
    login_url = '/accounts/login/'
    model = Meal

    # paginate_by = 1  # if pagination is desired

    def get_context_data(self, **kwargs):
        current_month = datetime.datetime.now().month
        context = super().get_context_data(**kwargs)
        context['object_list'] = Meal.objects.filter(user_id=self.request.user.pk,
                                                     meal_date__month=current_month).order_by(
            'meal_date')
        context['meal_count'] = Meal.objects.count()
        return context


class MealUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'meals/update.html'
    model = Meal
    form_class = UpdateMealForm
    login_url = '/accounts/login/'

    def form_valid(self, form):
        meal = form.save(commit=False)
        meal.user_id = self.request.user.pk
        meal.save()
        messages.success(self.request, 'A meal updated successfully.')
        return HttpResponseRedirect(reverse('meal-update', kwargs={'pk': meal.pk}))
