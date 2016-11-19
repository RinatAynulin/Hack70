from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import Course

# def course_view(request, *args, **kwargs):
#     print(request, args, kwargs)

class CourseView(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'courses/course.html'
