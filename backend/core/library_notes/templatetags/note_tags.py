from django import template
from library_notes.models import *


register = template.Library()


@register.simple_tag()
def get_themes():
    return Theme.objects.all()
