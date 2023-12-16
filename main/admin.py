from django.contrib import admin
from main.models import *

# Register your models here.
class AdminModelSingle(admin.ModelAdmin):
    pass


admin.site.register(Diagram, AdminModelSingle)
admin.site.register(UserProfile, AdminModelSingle)
admin.site.register(UserProfit, AdminModelSingle)
admin.site.register(UserTransaction, AdminModelSingle)
