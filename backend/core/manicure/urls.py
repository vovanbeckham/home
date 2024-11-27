

from django.urls import path

from manicure import views as vs


urlpatterns = [
    path('', vs.index, name='manicure'),
    path('by-services/', vs.by_services, name='manicure_by_services'),
    path('by-dates/', vs.by_dates, name='manicure_by_dates'),
]