from django.contrib import admin

# Register your models here.
from .models import *

class User_Info_Admin(admin.ModelAdmin):
    list_display = ('uid','name','pic_url','text','dateTime')
admin.site.register(User_Info,User_Info_Admin)
