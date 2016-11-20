from django.conf.urls import url, include
from .views import DocDetail, DocsListAjax

urlpatterns = [
    url(r'^(?P<chair_slug>\w+)/(?P<course_slug>\w+)/docs/(?P<pk>\d+)/$', DocDetail.as_view(), name='doc'),
    url(r'^(?P<chair_slug>\w+)/(?P<course_slug>\w+)/docs_ajax/$', DocsListAjax.as_view(), name='docs_ajax'),
]