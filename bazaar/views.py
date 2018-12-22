import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView
from django.views.generic.edit import FormMixin

from bazaar.forms import UpdateBazaarForm, AddBazaarForm, BazaarSearchForm
from bazaar.models import Bazaar


class BazaarCreateView(LoginRequiredMixin, CreateView):
    template_name = 'bazaar/add.html'
    login_url = 'accounts/login/'
    form_class = AddBazaarForm

    def form_valid(self, form):
        bazaar = form.save(commit=False)
        bazaar.user_id = self.request.user.pk
        bazaar.save()
        messages.success(self.request, 'A bazaar entry added successfully.')
        return HttpResponseRedirect(reverse('bazaar-add'))


class BazaarListView(LoginRequiredMixin, FormMixin, ListView):
    template_name = 'bazaar/list.html'
    login_url = 'accounts/login/'
    model = Bazaar
    form_class = BazaarSearchForm

    # paginate_by = 1  # if pagination is desired

    def get_context_data(self, **kwargs):
        current_month = datetime.datetime.now().month
        context = super().get_context_data(**kwargs)
        context['object_list'] = Bazaar.objects.select_related('user').filter(user_id=self.request.user.pk,
                                                                              bazaar_date__month=current_month).order_by(
            'bazaar_date')
        return context


class BazaarUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'bazaar/update.html'
    model = Bazaar
    form_class = UpdateBazaarForm
    login_url = 'accounts/login/'

    def form_valid(self, form):
        bazaar = form.save(commit=False)
        bazaar.user_id = self.request.user.pk
        bazaar.save()
        messages.success(self.request, 'A bazaar entry updated successfully.')
        return HttpResponseRedirect(reverse('bazaar-update', kwargs={'pk': bazaar.pk}))


class BazaarSearchView(LoginRequiredMixin, FormMixin, ListView):
    template_name = 'bazaar/list.html'
    login_url = '/accounts/login/'
    model = Bazaar
    form_class = BazaarSearchForm

    def get_queryset(self):
        from_date_day = int(self.request.GET.get('from_date_day'))
        from_date_month = int(self.request.GET.get('from_date_month'))
        from_date_year = int(self.request.GET.get('from_date_year'))
        to_date_day = int(self.request.GET.get('to_date_day'))
        to_date_month = int(self.request.GET.get('to_date_month'))
        to_date_year = int(self.request.GET.get('to_date_year'))
        member = int(self.request.GET.get('member'))

        from_date = datetime.date(from_date_year, from_date_month, from_date_day)
        to_date = datetime.date(to_date_year, to_date_month, to_date_day)
        object_list = Bazaar.objects.select_related('user').filter(user_id=member,
                                                                   bazaar_date__range=(from_date, to_date)).order_by(
            'bazaar_date')

        return object_list


class AccountingBazaarListView(LoginRequiredMixin, FormMixin, ListView):
    template_name = 'bazaar/list.html'
    login_url = 'accounts/login/'
    model = Bazaar
    form_class = BazaarSearchForm

    # paginate_by = 1  # if pagination is desired

    def get_context_data(self, **kwargs):
        current_month = datetime.datetime.now().month
        context = super().get_context_data(**kwargs)
        context['object_list'] = Bazaar.objects.filter(bazaar_date__month=current_month).order_by(
            'bazaar_date')
        return context
