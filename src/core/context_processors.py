from django.contrib.auth.views import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

def context_login(request, *args, **kwargs):
    # if request.method == 'POST':
    #     form = AuthenticationForm(request.POST, data=request.POST)
    #     if form.is_valid():
    #         username = request.POST['username']
    #         password = request.POST['password']
    #         user = authenticate(username=username, password=password)
    #         login(request, user)
    #     return {'authform': form}


    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return {}
    #     else:
    #         return {'authform' : form}
    # print('GET')
    return {'authform': AuthenticationForm()}