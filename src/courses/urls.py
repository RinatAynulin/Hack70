from django.conf.urls import url, include
from .views import CourseView

urlpatterns = [
    url(r'^(?P<chair_slug>\w+)/(?P<pk>\d+)/$', CourseView.as_view(), name='course'),
]