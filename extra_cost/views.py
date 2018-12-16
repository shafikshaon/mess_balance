import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import UpdateView, ListView, CreateView

from extra_cost.forms import UpdateExtraCostForm, AddExtraCostForm
from extra_cost.models import ExtraCost


class ExtraCostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'extra_cost/add.html'
    login_url = 'accounts/login/'
    form_class = AddExtraCostForm

    def form_valid(self, form):
        bazaar = form.save(commit=False)
        bazaar.user_id = self.request.user.pk
        bazaar.save()
        return HttpResponseRedirect(reverse('extra_cost-add'))


class ExtraCostListView(LoginRequiredMixin, ListView):
    template_name = 'extra_cost/list.html'
    login_url = 'accounts/login/'

    model = ExtraCost

    # paginate_by = 1  # if pagination is desired

    def get_context_data(self, **kwargs):
        current_month = datetime.datetime.now().month
        context = super().get_context_data(**kwargs)
        context['object_list'] = ExtraCost.objects.filter(user_id=self.request.user.pk,
                                                          expense_date__month=current_month).order_by(
            'expense_date')
        return context


class ExtraCostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'extra_cost/update.html'
    model = ExtraCost
    form_class = UpdateExtraCostForm
    login_url = 'accounts/login/'
    success_message = 'A project updated successfully.'

    def form_valid(self, form):
        extra_cost = form.save(commit=False)
        extra_cost.user_id = self.request.user.pk
        extra_cost.save()
        return HttpResponseRedirect(reverse('extra_cost-update', kwargs={'pk': extra_cost.pk}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
