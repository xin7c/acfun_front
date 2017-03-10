from django.contrib import admin
from .models import *


class MOBILE_API_Admin(admin.ModelAdmin):
    list_display = ('id', 'api_name', 'api_version', 'api_device', 'auto_time')
    search_fields = ['id', 'api_name', 'api_version', 'api_device', 'auto_time']
    list_select_related = (True)
    list_display_links = ('id', 'api_name', 'api_version', 'api_device', 'auto_time')




class API_VERSION_Admin(admin.ModelAdmin):
    list_display = ('id', 'api_version')
    search_fields = ['id', 'api_version']
    list_select_related = (True)
    list_display_links = ('id', 'api_version')

admin.site.register(MOBILE_API, MOBILE_API_Admin)
admin.site.register(API_VERSION, API_VERSION_Admin)
