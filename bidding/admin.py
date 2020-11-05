from django.contrib import admin

from .models import Client
from .models import Sinfo
#from .models import Iinfo


admin.site.register(Client)
admin.site.register(Sinfo)
# class ClientAdmin(admin.ModelAdmin):
#    list_display = ['fname', 'lname', 'mailid', 'sex', 'age']
