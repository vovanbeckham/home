
from django.db.models import Sum


import datetime
from manicure.models import ProvidedService


def get_data_service():

    today = datetime.date.today() - datetime.timedelta(days=5)
    first_day_month_now = datetime.date(today.year, today.month, 1)
    last_month = first_day_month_now - datetime.timedelta(days=20)
    first_day_month_last = datetime.date(last_month.year, last_month.month, 1)
    data_month = ProvidedService.objects.filter(
        date__gte=first_day_month_now
        ).values(
            'service__short', 
            'service__base__name'
            ).annotate(Sum('price')).order_by('-price__sum')
    data_list = []
    data_last_month = ProvidedService.objects.filter(
        date__gte=first_day_month_last, 
        date__lt=first_day_month_now
        ).values(
            'service__short', 
            'service__base__name'
            ).annotate(
                Sum('price')
                ).order_by('-price__sum')
    data_list = []
    data = []
    label = []
    sum = 0
    for service in data_month:
        label.append('%s %s' % (service['service__base__name'], service['service__short']))
        data.append(float(service['price__sum']))
        sum += service['price__sum']
    data_list.append({'month': first_day_month_now, 'data': data, 'label': label, 'sum': float(sum)})
    data = []
    label = []
    sum = 0
    for service in data_last_month:
        label.append('%s %s' % (service['service__base__name'], service['service__short']))
        data.append(float(service['price__sum']))
        sum += service['price__sum']
    data_list.append({'month': first_day_month_last, 'data': data, 'label': label, 'sum': float(sum)})
    return data_list