import datetime
from django.http import HttpResponse
from django.shortcuts import render

from manicure.models import ProvidedService, Service




def index(request):
    last_day_week = datetime.datetime.now() - datetime.timedelta(days=7)
    services = ProvidedService.objects.filter(date__gte=last_day_week).order_by('date')
    return render(request, "index.html", locals())
