

from django.urls import path

from home import views as vs


urlpatterns = [
    path('test/', vs.home, name='home'),
]






# API


urlpatterns += [
    path('api/v1/add/', vs.AddSensorValue.as_view(), name='add_sensor_value'),

]