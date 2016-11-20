from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.decorators.http import require_POST
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


def course_members(request, chair_slug, course_slug):
    members = Course.objects.get(slug=course_slug).members.all()
    test = 'test'
    print(chair_slug)
    print(course_slug)
    return render(request, 'courses/members.html', {'members': members, 'test': test})


class MembersListAjax(ListView):
    model = Course
    template_name = 'courses/members.html'
    context_object_name = 'members'

    def get_queryset(self):
        return Course.objects.get(slug=self.kwargs['course_slug']).members.all()


@login_required
@require_POST
def add_course(request, chair_slug, course_slug):
    message = "success"
    if request.method == 'POST':
        user = request.user
        course = get_object_or_404(Course, slug=course_slug)

        if course.members.filter(id=user.id).exists():
            # user has already liked this company
            # remove like/user
            message = 'You\'ve already added this'
        else:
            course.members.add(user)

    ctx = {'message': message}
    # use mimetype instead of content_type if django < 5
    return JsonResponse(ctx)
