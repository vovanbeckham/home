import datetime
from django.http import HttpResponse
from django.shortcuts import render

from manicure.models import ProvidedService, Service




def index(request):
    menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]
    today = datetime.datetime.now()
    services = ProvidedService.objects.all()
    return render(request, "index.html", locals())
