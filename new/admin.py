from django.contrib import admin
from new.models import Newsletter
# Register your models here.

class AdminNewsletter(admin.ModelAdmin):
    list_display=("email", "date_inscription")
    
admin.site.register(Newsletter,AdminNewsletter)