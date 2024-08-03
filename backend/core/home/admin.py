from django.contrib import admin

from home.models import *


admin.site.register(Device)
admin.site.register(Sensor)
admin.site.register(SensorValue)
admin.site.register(SensorValueAvgDay)
