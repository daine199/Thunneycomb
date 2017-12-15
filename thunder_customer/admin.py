#! /usr/bin/env python

"""
# Owner Daine.H
# Modify 2017-12-15
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile
# Register your models here.


class ProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False


class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
