
from django.db.models import Sum


from libs.functions import get_month
from manicure.models import ProvidedService


def get_data_service():
    dates = get_month()
    data_list = []
    for date in dates:
        data = []
        label = []
        sum = 0
        data_month = ProvidedService.objects.filter(
            date__gte=date[0],
            date__lt=date[1]
            ).values(
                'service__short', 
                'service__base__name'
                ).annotate(Sum('price')).order_by('-price__sum')
        
    
        for service in data_month:
            label.append('%s %s' % (
                service['service__base__name'], 
                service['service__short']
                ))
            data.append(float(service['price__sum']))
            sum += service['price__sum']
        if data:
            data_list.append({'month': date[0], 'data': data, 'label': label, 'sum': float(sum)})

    return data_list