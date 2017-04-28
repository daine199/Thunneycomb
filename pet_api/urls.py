#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Daine.H
from django.conf.urls import url

from pet_api import views

urlpatterns = [
    url(r'^api_test$', views.pet_get, name='pet_api'),
]
