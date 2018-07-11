#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Daine.H

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^init-sms-sender/$', views.init_sms_sender, name='init_base_components'),

]
