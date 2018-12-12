#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Daine.H

from django.conf.urls import url
from basis_components.views import sendMailViews


urlpatterns = [
    url(r'^init-sms-sender/$', sendMailViews.init_sms_sender, name='init_base_components'),
    url(r'^send-sms/$', sendMailViews.send_code, name='send_code'),

]
