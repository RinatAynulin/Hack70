from django.conf.urls import url, include
from .views import PostView

urlpatterns = [
    url(r'^(?P<chair_slug>\w+)/(?P<course_slug>\w+)/posts/(?P<pk>\d+)/$', PostView.as_view(), name='discussion'),
]