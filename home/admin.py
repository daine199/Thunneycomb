#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Entrance, EntrancePermission


class EntranceAdmin(admin.ModelAdmin):
    list_display = ('id', 'entrance', 'entrance_url')


class EntrancePermissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'has_index_perm')


admin.site.register(Entrance, EntranceAdmin)
admin.site.register(EntrancePermission, EntrancePermissionAdmin)
