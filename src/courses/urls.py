from django.conf.urls import url, include

from courses.views import course_page, course_info, course_members, add_course, MembersListAjax

urlpatterns = [
    url(r'^(?P<chair_slug>\w+)/(?P<course_slug>\w+)/$', course_page, name='course_page'),
    url(r'^(?P<chair_slug>\w+)/(?P<course_slug>\w+)/info$', course_info, name='course_info'),
    url(r'^(?P<chair_slug>\w+)/(?P<course_slug>\w+)/members$', MembersListAjax.as_view(), name='course_members'),
    url(r'^(?P<chair_slug>\w+)/(?P<course_slug>\w+)/add$', add_course, name='add_course'),
]