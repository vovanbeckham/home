from django.contrib import admin


from expenses.models import *


admin.site.register(Source)
admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(Transfer)