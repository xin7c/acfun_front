from django.contrib import admin
from .models import Frontdb


class FrontdbAdmin(admin.ModelAdmin):
    list_display = ('id', 'projectName', 'timestamp')


admin.site.register(Frontdb, FrontdbAdmin)
