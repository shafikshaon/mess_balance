import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from meals.forms import AddMealForm, UpdateMealForm
from meals.models import Meal


@method_decorator([login_required(login_url='/admin/login/')], name='dispatch')
class MealCreateView(CreateView):
    template_name = 'meals/add.html'
    form_class = AddMealForm

    def form_valid(self, form):
        meal = form.save(commit=False)
        meal.user_id = self.request.user.pk
        meal.save()
        return HttpResponseRedirect(reverse('meal-add'))


@method_decorator([login_required(login_url='/admin/login/')], name='dispatch')
class MealListView(ListView):
    template_name = 'meals/list.html'

    model = Meal

    # paginate_by = 1  # if pagination is desired

    def get_context_data(self, **kwargs):
        current_month = datetime.datetime.now().month
        context = super().get_context_data(**kwargs)
        context['object_list'] = Meal.objects.filter(user_id=self.request.user.pk, meal_date__month=current_month).order_by(
            'meal_date')
        return context


@method_decorator([login_required(login_url='/admin/login/')], name='dispatch')
class MealUpdateView(UpdateView):
    template_name = 'meals/update.html'
    model = Meal
    form_class = UpdateMealForm
    success_message = 'A project updated successfully.'

    def form_valid(self, form):
        meal = form.save(commit=False)
        meal.user_id = self.request.user.pk
        meal.save()
        return HttpResponseRedirect(reverse('meal-update', kwargs={'pk': meal.pk}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

