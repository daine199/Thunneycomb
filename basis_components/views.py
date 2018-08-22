#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Daine.H

from django.contrib.auth.decorators import permission_required
from .api.sendSmsApi import init_default_sender, send_code_sms
from django.shortcuts import redirect


# Create your views here.


@permission_required('basis_components.change_smssender')
def init_sms_sender(request):
    init_default_sender()
    return redirect('/')


def send_code(request):
    phone_no = None
    if "GET" == request.method:
        phone_no = request.GET.get("phone_no")
    if "POST" == request.method:
        phone_no = request.POST.get("phone_no")
    if phone_no is not None:
        send_code_sms(phone_no)
    return redirect('/')



