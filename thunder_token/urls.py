#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Daine.H
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create$', views.create_token, name='create_token'),
    url(r'^token-login$', views.token_login, name='token_login'),
]
