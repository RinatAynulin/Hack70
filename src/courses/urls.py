from django.conf.urls import url, include

from courses.views import course_page

urlpatterns = [
    url(r'^$', course_page, name='mainpage'),
]