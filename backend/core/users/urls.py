
from django.urls import path
from django.contrib.auth.views import LogoutView
from users import views as dv


urlpatterns = [
    path('login/', dv.LoginUser.as_view(), name='login'),
    path('logout/', dv.logout_view, name='logout'),
    path('register/', dv.register, name='register'),
]