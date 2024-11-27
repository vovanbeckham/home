
from django.shortcuts import redirect, render
from django.contrib import messages

from manicure.functions import get_data_service




def index(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Доступ запрещен!')
        return redirect('notes-index')
    service_dict = get_data_service()


    return render(request, "manicure/index.html", locals())


def by_services(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Доступ запрещен!')
        return redirect('notes-index')
    service_dict = get_data_service()


    return render(request, "manicure/by_services.html", locals())




def by_dates(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Доступ запрещен!')
        return redirect('notes-index')
    service_dict = get_data_service()

    print("HERE")
    return render(request, "manicure/by_dates.html", locals())