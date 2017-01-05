#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from .models import Entrance
from django.core import exceptions
from django.shortcuts import redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from .lib.deploy_tool import check_deploy_perms, deploy_app
from django.views.decorators.csrf import csrf_exempt

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


def login_user(request, *args, **kwargs):
    if request.method == 'GET':
        next_page = request.GET.get('next')
        if not request.user.is_authenticated():
            if next_page is not None:
                request.session['next'] = next_page
            return render(request, 'home/login.html')
        else:
            if next_page is not None:
                return redirect("/{next}".format(next=next_page))
            else:
                return redirect("/")
    if request.method == 'POST':
        userid = request.POST.get('userid')
        password = request.POST.get('password')
        user = authenticate(username=userid, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                next_page = request.session.get('next', '/')
                print(next_page)
                if next_page is not None:
                    return redirect("{next}".format(next=next_page))
                else:
                    return redirect("/")
            else:
                context = {"error": "Disable UserID {}".format(userid)}
                return render(request, 'home/login.html', context)
        else:
            context = {"error": "Unknown UserID {}".format(userid)}
            return render(request, 'home/login.html', context)


def logout_processor(request):
    if request.user.is_authenticated():
        logout(request)
        return redirect("/")
    else:
        return redirect("/")


# @login_required()
@csrf_exempt
def deploy_entrance(request):
    if request.method == 'GET':
        #  TODO add deploy template and render a post page
        return redirect("/")
    if request.method == 'POST':
        if check_deploy_perms(request.user):
            #  TODO Do something deploy
            app_name = request.POST.get('app_name')
            app_version = request.POST.get('app_version')
            res = deploy_app(app_name, app_version)
            #  TODO rewrite deploy loading page.
            return HttpResponse(res)
        else:
            context = {"error": "No Deploy Access."}
            return render(request, 'home/entrance.html', context)
    else:
        return redirect(reverse('home.index_page'))


@login_required()
class EntranceViewSet(viewsets.ModelViewSet):
    queryset = Entrance.objects.all()
    serializer_class = EntranceSerializer


@login_required()
def index(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            return render(request, 'home/index.html')
        else:
            return redirect("/")


