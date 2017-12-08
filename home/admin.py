#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Entrance, Switch


class EntranceAdmin(admin.ModelAdmin):
    list_display = ('id', 'entrance', 'entrance_url')


class SwitchAdmin(admin.ModelAdmin):
    list_display = ('switch_key', 'Switch_value')


admin.site.register(Entrance, EntranceAdmin)
admin.site.register(Switch, SwitchAdmin)
