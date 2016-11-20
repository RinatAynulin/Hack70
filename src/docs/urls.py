from django.conf.urls import url, include
from .views import DocsDetail, DocsListAjax

urlpatterns = [
    url(r'^(?P<chair_slug>\w+)/(?P<course_slug>\w+)/posts/(?P<pk>\d+)/$', DocsDetail.as_view(), name='discussion'),
    url(r'^(?P<chair_slug>\w+)/(?P<course_slug>\w+)/discussions_ajax/$', DocsListAjax.as_view(), name='discussions_ajax'),
]