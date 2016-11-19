from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from courses.models import Chair, Course


def course_page(request):
    return render(request, 'courses/course_page.html')


class ChairList(ListView):
    template_name = 'courses/chairs.html'
    context_object_name = 'chairs'
    model = Chair

    def get_queryset(self):
        return Chair.objects.all()


class CourseList(ListView):
    template_name = 'courses/courses.html'
    context_object_name = 'courses'
    model = Course


    def get_queryset(self):
        return Course.objects.all()
