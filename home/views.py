#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from .models import Entrance, Switch
from django.core import exceptions
from django.shortcuts import redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from .lib.deploy_tool import check_deploy_perms, deploy_app
import json
import logging


from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import viewsets
from .serializers import EntranceSerializer


# Create your views here.

# Get an instance of a logger
logger = logging.getLogger(__name__)


def entrance(request):
    if request.method == 'GET':
        logger.info('Get to the Entrance.')
        return render(request, 'home/entrance.html')
    if request.method == 'POST':
        app_name = request.POST.get('app_name').lower()
        logger.info('Got APP {app_name}'.format(app_name=app_name))

        try:
            logger.info('Try Find {app_name} Entrance.'.format(app_name=app_name))
            ent = Entrance.objects.get(entrance=app_name)
            logger.info('Got {app_name} Entrance.'.format(app_name=app_name))
        except exceptions.ObjectDoesNotExist:
            logger.info('Got {app_name} Entrance Failed.'.format(app_name=app_name))

        try:
            logger.info('Check wiki Search Switch.')
            wiki_search_key = Switch.objects.get(switch_key="is_wiki_search_open")
        except exceptions.ObjectDoesNotExist:
            logger.info('wiki Search Switch Disable.')
            wiki_search_key = False

        if wiki_search_key:
            return redirect("./wiki/_search/?q={0}".format(app_name))
        else:
            # 同一IP多次请求非法入口时拒绝服务并跳转外站
            logger.warning('{app_name} Entrance not found.'.format(app_name=app_name))
            invalid_ip = str(request.META.get("REMOTE_ADDR", None))
            invalid_time = request.session.get(invalid_ip, 1)
            if int(invalid_time) > 3:
                logger.error('Wrong Entrance input > 3, Reject requests.')
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


# @csrf_exempt
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


@login_required()
def deploy_entrance(request):
    if request.method == 'GET':
        #  TODO add deploy template and render a post page
        return render(request, 'home/deploy.html')
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


def my_view(request):
    print(__name__)
    content = {"logging": True}
    logger.info('info')
    logger.debug('debug! ')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')
    return HttpResponse(json.dumps(content), content_type='application/javascript;charset=utf-8')


# @csrf_exempt
# @login_required
def post_test(request):
    content = {'method': ''}
    if request.method == 'GET':
        # content['method'] = 'GET'
        content['content'] = request.GET
        # content['header'] = str(request.META)
    if request.method == 'POST':
        content['method'] = 'POST'
        data = request.POST
        # header = request.META
        content['content'] = data
        # content['header'] = str(header)
        print(data)
    return HttpResponse(json.dumps(content))
