
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

from users.forms import LoginUserForm, RegisterUserForm



class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}



def logout_view(request):
    logout(request)
    return redirect('notes-index')


def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) 
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('notes-index')
    else:
        form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form})