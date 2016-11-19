# coding: utf-8

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.conf import settings
from django.http import request, HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse

from .models import User
from .forms import RegistrationForm


class UserView(DetailView):
    model = User
    template_name = 'core/user.html'
    slug_field = 'username'
    context_object_name = 'user_account'

    def get_context_data(self, **kwargs):
        context = super(UserView, self).get_context_data(**kwargs)
        context['profile'] = self.request.user
        return context


class UserEdit(UpdateView):
    model = User
    template_name = 'core/user_edit.html'
    fields = ('email', 'first_name', 'last_name', 'avatar')
    slug_field = 'username'

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk)

        # def get_queryset(self):
        #     return User.objects.filter(username=self.request.user.username)


class RegisterView(CreateView):
    model = User
    template_name = 'core/registration/registration_form.html'
    form_class = RegistrationForm
    success_url = 'core:login'

    def get_success_url(self):
        return reverse(self.success_url)


def home(request):
    return render(request, 'core/home.html')
