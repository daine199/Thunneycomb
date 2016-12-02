from django.contrib import admin
from .models import Entrance


class EntranceAdmin(admin.ModelAdmin):
    list_display = ('id', 'entrance', 'entrance_url')


admin.site.register(Entrance, EntranceAdmin)
