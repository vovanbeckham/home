from django.contrib import admin

from manicure.models import *


admin.site.register(TelegramUser)
admin.site.register(BaseService)
admin.site.register(Service)
admin.site.register(ProvidedService)
