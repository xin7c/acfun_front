from django.contrib import admin
from .models import MOBILE_API


class MOBILE_API_Admin(admin.ModelAdmin):
    list_display = ('id', 'api_name', 'api_version', 'api_device')
    search_fields = ['id']
    list_select_related = (True)
    list_display_links = ('id', 'api_name', 'api_version', 'api_device')

admin.site.register(MOBILE_API, MOBILE_API_Admin)
