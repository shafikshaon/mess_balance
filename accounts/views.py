from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.base import View

from accounts.forms.login import LoginForm
from accounts.forms.user import AddUserForm, UpdateUserForm
from accounts.models import User


class LoginView(View):
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.data['username'], password=form.data['password'])
            if user is not None:
                login(request, user)
            return HttpResponseRedirect('/')

        return render(request, self.template_name)


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/accounts/login/')


class UserCreateView(LoginRequiredMixin, CreateView):
    template_name = 'accounts/add.html'
    login_url = '/accounts/login/'
    form_class = AddUserForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.user_id = self.request.user.pk
        user.save()
        messages.success(self.request, 'An user added successfully.')
        return HttpResponseRedirect(reverse('user-add'))


class UserListView(LoginRequiredMixin, ListView):
    template_name = 'accounts/list.html'
    login_url = '/accounts/login/'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = User.objects.order_by(
            'created_at')
        context['object_count'] = User.objects.count()
        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/update.html'
    model = User
    form_class = UpdateUserForm
    login_url = '/accounts/login/'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.password1 = user.set_password(user.password)
        user.user_id = self.request.user.pk
        user.save()
        messages.success(self.request, 'An user information updated successfully.')
        return HttpResponseRedirect(reverse('user-update', kwargs={'pk': user.pk}))
