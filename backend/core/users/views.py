
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

from users.forms import LoginUserForm



class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}



def logout_view(request):
    logout(request)
    return redirect('home')