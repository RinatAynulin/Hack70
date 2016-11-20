# coding: utf-8
import feedparser
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.conf import settings
from django.http import request, HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse

from courses.models import Chair, Course
from .models import User
from .forms import RegistrationForm, NavSearchForm


class UserView(DetailView):
    model = User
    template_name = 'core/user_profile.html'
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


class CourseSearch(ListView):
    template_name = 'core/search.html'
    context_object_name = 'courses'
    model = Course
    form_class = NavSearchForm

    def get_queryset(self):
        if self.q:
            return Course.objects.filter(Q(description__contains=self.q) | Q(title__contains=self.q))
        return Course.objects.all()

    def dispatch(self, request, *args, **kwargs):
        self.q = ""
        self.search_form = NavSearchForm(request.GET or None)
        if self.search_form.is_valid():
            self.q = self.search_form.cleaned_data['q']
        return super(CourseSearch, self).dispatch(request, *args, **kwargs)


def home(request):
    chairs = Chair.objects.all()
    return render(request, 'core/home.html', {'chairs': chairs})


def courses(request, chair_slug):
    courses = Chair.objects.get(slug=chair_slug).chair_courses.all()
    return render(request, 'core/courses.html', {'courses': courses})


def mipt_news(request):
    feeds = feedparser.parse('https://mipt.ru/news/rss.php')
    return render(request, 'core/rss.html', {'feeds': feeds})


def user_courses(request):
    return render(request, 'core/user_courses.html')

def video_useless(request):
    return render(request, 'core/video_useless.html')

def guides_temp(request):
    return render(request, 'core/guides_temp.html')
