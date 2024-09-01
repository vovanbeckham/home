from django import template
from home.models import Device


register = template.Library()


@register.simple_tag()
def get_device():
    return Device.objects.all()
