

from django.urls import path

from home import views as vs


urlpatterns = [
    path('', vs.home, name='home'),
    path('graph/device/<int:device_id>/', vs.graph_device, name='graph_device'),
]






# API


urlpatterns += [
    path('api/v1/add/', vs.AddSensorValue.as_view(), name='add_sensor_value'),

]