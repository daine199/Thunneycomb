#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .rest_view_set import EntranceViewSet, SwitchViewSet
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
]

#  Deploy ROUTER
urlpatterns += [
    path(r'deploy/', views.deploy_entrance, name='deploy_entrance')
]

# Rest Admin
router = routers.DefaultRouter()
router.register(r'Entrances', EntranceViewSet)
router.register('Switch', SwitchViewSet)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^home/', include(router.urls))
]

