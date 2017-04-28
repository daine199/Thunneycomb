#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Daine.H
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^api-test$', views.apt_test, name='pet_api'),
]
