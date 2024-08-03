

from django.urls import path

from manicure import views as vs


urlpatterns = [
    path('', vs.index, name='index'),
]