#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path
from .admin import admin_site

from home import views

urlpatterns = [
    path('', views.entrance, name='entrance_page')
]

urlpatterns += [
    path('myadmin/', admin_site.urls),
    path('sysadmin/', admin.site.urls)
]


urlpatterns += [
    path('index/', views.index),
    path('accounts/login/', views.login_user, name='login_page'),
    path('logout/', views.logout_processor, name='logout_processor')
]

#  Deploy ROUTER
urlpatterns += [
    path('deploy/', views.deploy_entrance, name='deploy_entrance')
]


