import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView

from bazaar.forms import UpdateBazaarForm, AddBazaarForm
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


class BazaarListView(LoginRequiredMixin, ListView):
    template_name = 'bazaar/list.html'
    login_url = 'accounts/login/'
    model = Bazaar

    # paginate_by = 1  # if pagination is desired

    def get_context_data(self, **kwargs):
        current_month = datetime.datetime.now().month
        context = super().get_context_data(**kwargs)
        context['object_list'] = Bazaar.objects.filter(user_id=self.request.user.pk,
                                                       bazaar_date__month=current_month).order_by(
            'bazaar_date')
        context['bazaar_entry_count'] = Bazaar.objects.filter(user_id=self.request.user.pk,
                                                              bazaar_date__month=current_month).count()
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
