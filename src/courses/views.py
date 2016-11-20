from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from django.views.generic import ListView

from courses.models import Chair, Course


def course_page(request, chair_slug, course_slug):
    chair = Chair.objects.get(slug=chair_slug)
    course = Course.objects.get(slug=course_slug)
    return render(request, 'courses/course_page.html', {'chair': chair, 'course': course})


def course_info(request, chair_slug, course_slug):
    chair = Chair.objects.get(slug=chair_slug)
    course = Course.objects.get(slug=course_slug)
    return render(request, 'courses/course_info.html', {'chair': chair, 'course': course})
