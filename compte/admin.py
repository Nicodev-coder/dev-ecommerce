from django.contrib import admin
from compte.models import Client

class AdminUser(admin.ModelAdmin):
    list_display=("username","password")

admin.site.register(Client,AdminUser)
# Register your models here.
