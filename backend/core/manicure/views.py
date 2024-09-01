
from django.shortcuts import render

from manicure.functions import get_data_service




def index(request):
    service_dict = get_data_service()


    return render(request, "manicure/index.html", locals())
