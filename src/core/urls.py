from django.conf.urls import url, include
from .views import home, UserView, RegisterView, UserEdit, courses
from django.contrib import admin
from django.contrib.auth.views import login, logout, password_change
from django.contrib.auth.decorators import login_required, user_passes_test
from application.settings import LOGIN_URL


# def redirect_authenticated(function=None):
#     from django.urls import reverse
#     actual_decorator = user_passes_test(
#         lambda u: u.is_anonymous,
#         login_url=reverse('core:mainpage'),
#     )
#     if function:
#         return actual_decorator(function)
#     return actual_decorator

urlpatterns = [
    url(r'^$', home, name='mainpage'),
    url(r'^accounts/logout/$', login_required(logout, login_url=LOGIN_URL), {'next_page' : '/'}, name='logout'),
    url(r'^accounts/login/$', login,{'template_name' : 'core/registration/login.html',
                                     'redirect_authenticated_user': True,
                                     }, name='login'),
    url(r'^accounts/password_change/$',
        login_required(password_change, login_url=LOGIN_URL),{'template_name':'core/registration/password_change.html', 'post_change_redirect':'/'},
        name='password_change'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', RegisterView.as_view(), name='register'),
    url(r'^users/(?P<slug>\w+)/$', login_required(UserView.as_view(), login_url=LOGIN_URL), name="user"),
    url(r'^accounts/user_edit/$', login_required(UserEdit.as_view(), login_url=LOGIN_URL), name="user_edit"),
    url(r'^(?P<chair_slug>\w+)/$', courses, name='courses'),
]