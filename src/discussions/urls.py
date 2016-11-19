from django.conf.urls import url, include
from .views import PostDetail

urlpatterns = [
    url(r'^(?P<chair_slug>\w+)/(?P<course_slug>\w+)/posts/(?P<pk>\d+)/$', PostDetail.as_view(), name='discussion'),
]