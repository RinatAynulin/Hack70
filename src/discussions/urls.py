from django.conf.urls import url, include
from .views import PostDetail, PostListAjax

urlpatterns = [
    url(r'^(?P<chair_slug>\w+)/(?P<course_slug>\w+)/posts/(?P<pk>\d+)/$', PostDetail.as_view(), name='discussion'),
    url(r'^(?P<chair_slug>\w+)/(?P<course_slug>\w+)/discussions_ajax/$', PostListAjax.as_view(), name='discussions_ajax'),
]