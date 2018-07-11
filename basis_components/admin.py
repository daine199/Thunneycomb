#! /usr/bin/env python

"""
# Owner Daine.H
# Modify 2017-12-25
"""
from django.contrib import admin
from .models import MySubMail, SmsSender

# Register your models here.


class MySubMailAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_no', 'code')


class SmsSenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender_name', 'template')


admin.site.register(MySubMail, MySubMailAdmin)
admin.site.register(SmsSender, SmsSenderAdmin)
