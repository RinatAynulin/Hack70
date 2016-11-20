from django.conf.urls import url, include

from courses.views import course_page, course_info

urlpatterns = [
    url(r'^(?P<chair_slug>\w+)/(?P<course_slug>\w+)/$', course_page, name='course_page'),
    url(r'^(?P<chair_slug>\w+)/(?P<course_slug>\w+)/info$', course_info, name='course_info'),
]