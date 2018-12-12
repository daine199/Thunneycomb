#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Daine.H
import logging

from django.contrib.auth.decorators import permission_required
from ..api.sendSmsApi import init_default_sender, send_code_sms
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
# Get an instance of a logger
logger = logging.getLogger(__name__)


@permission_required('basis_components.change_smssender')
def init_sms_sender(request):
    init_default_sender()
    return redirect('/')


@login_required()
def send_code(request):

    phone_no = None
    if "GET" == request.method:
        phone_no = request.GET.get("phone_no")
        # print(request.user.is_authenticated())
        logger.info(request.user.is_authenticated())
    if "POST" == request.method:
        phone_no = request.POST.get("phone_no")
    if phone_no is not None:
        send_code_sms(phone_no)
    return redirect('/')



