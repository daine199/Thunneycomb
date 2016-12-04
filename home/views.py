#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import Entrance
from django.core import exceptions
from django.shortcuts import redirect
from django.contrib.auth import logout

from rest_framework import viewsets
from .serializers import EntranceSerializer


# Create your views here.


def entrance(request):
    if request.method == 'GET':
        return render(request, 'home/entrance.html')
    if request.method == 'POST':
        app_name = request.POST.get('app_name').lower()
        try:
            ent = Entrance.objects.get(entrance=app_name)
        except exceptions.ObjectDoesNotExist:
            # 同一IP多次请求非法入口时拒绝服务并跳转外站
            invalid_ip = str(request.META.get("REMOTE_ADDR", None))
            invalid_time = request.session.get(invalid_ip, 1)
            if int(invalid_time) > 3:
                try:
                    ent = Entrance.objects.get(entrance="get_out")
                    out_site = ent.entrance_url
                except exceptions.ObjectDoesNotExist:
                    out_site = "http://www.baidu.com"
                return redirect(out_site)
            request.session[invalid_ip] = (invalid_time + 1)
            context = {"error": "Invalid Entrance {}".format(app_name)}
            return render(request, 'home/entrance.html', context)
        return redirect(ent.entrance_url)


def login_processor(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            return redirect("/")
        else:
            return redirect("/login_page")


def logout_processor(request):
    if request.user.is_authenticated():
        logout(request)
        return redirect("/")
    else:
        return redirect("/")


class EntranceViewSet(viewsets.ModelViewSet):
    queryset = Entrance.objects.all()
    serializer_class = EntranceSerializer


def index(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            return render(request, 'home/index.html')
        else:
            return redirect("/")






