from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.base import View


class DashboardView(LoginRequiredMixin, View):
    template_name = 'core/dashboard.html'
    login_url = 'accounts/login/'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
