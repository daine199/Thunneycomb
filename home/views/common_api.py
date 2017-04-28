#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Daine.H
from django.contrib.auth import login, BACKEND_SESSION_KEY
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework.authtoken.models import Token
import json

from home.lib.token_lib import TokenLoginBackend


@login_required()
def get_session(request):
    content = {}
    request_session = request.session
    content['userid'] = request.session['userid']
    content['sessionid'] = request_session.session_key
    print(str(dir(request_session)))
    print(request_session.keys())

    return HttpResponse(json.dumps(content), content_type='application/javascript;charset=utf-8')


def get_token(request):
    content = {'userid': None, 'token': None, 'backend': None}
    userid = request.session['userid']
    if userid:
        try:
            user_obj = User.objects.get(username=userid)
            backend = request.session[BACKEND_SESSION_KEY]
            content['userid'] = userid
            content['token'] = user_obj.user.auth_token
            content['backend'] = backend
        except User.DoesNotExist:
            pass
    else:
        pass
    return HttpResponse(json.dumps(content), content_type='application/javascript;charset=utf-8')


def token_login(request):
    content = {}
    cookie = request.COOKIES
    try:
        if cookie['token']:
            token_key = request.COOKIES['token']
    except KeyError:
        pass
    if request.method == 'GET':
        token_key = request.GET.get("token")
    if request.method == 'POST':
        token_key = request.POST.get('token')

    if not token_key:
        content['login_status'] = False
    else:
        user = TokenLoginBackend.authenticate(token_key)
        if user:
            login(request, user)
            content['token'] = token_key
            content['login_status'] = True

        else:
            content['login_status'] = False

    return HttpResponse(json.dumps(content), content_type='application/javascript;charset=utf-8')



