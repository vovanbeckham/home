import datetime
from django.http import HttpResponse
from django.shortcuts import render

from manicure.functions import get_data_service
from manicure.models import ProvidedService, Service




def index(request):
    service_dict = get_data_service()


    

    last_day_week = datetime.datetime.now() - datetime.timedelta(days=7)
    services = ProvidedService.objects.filter(date__gte=last_day_week).order_by('date')
    #test
    services = ProvidedService.objects.all().order_by('date')
    return render(request, "manicure/index.html", locals())
