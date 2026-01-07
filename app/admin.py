from django.contrib import admin
from app.models import Ebook,UserEbook

class AdminEbook(admin.ModelAdmin):
    list_display=("titre","description","slug","pdf","image","date_ajout")

class AdminUserEbookk(admin.ModelAdmin):
    list_display=("user","ebook","date_telechargement")

admin.site.register(UserEbook,AdminUserEbookk)
admin.site.register(Ebook,AdminEbook)
# Register your models here.

