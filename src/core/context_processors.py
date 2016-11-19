from django.contrib.auth.views import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

def context_login(request, *args, **kwargs):
    return {'authform': AuthenticationForm()}