#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Daine.H

from django.contrib.auth.decorators import permission_required
from .api.sendSmsApi import init_default_sender
from django.shortcuts import redirect


# Create your views here.


@permission_required('basis_components.change_smssender')
def init_sms_sender(request):
    init_default_sender()
    return redirect('/')

