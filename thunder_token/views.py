#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login

from django.http import HttpResponse
import json

# Create your views here.


@login_required()
def create_token(request):
    content = {'this': 'create_token', 'method': request.method}
    print("Create_token")
    # print(dir(request))
    # print(request.user, dir(request.session))
    user_obj = User.objects.get(username=request.user)

    try:
        user_token = Token.objects.get(user=user_obj)
        content['action'] = 'REBINDING'
    except Token.DoesNotExist:
        user_token = Token.objects.create(user=user_obj)
        content['action'] = 'CREATE'
        user_token.save()

    user_obj.auth_token = user_token
    user_obj.save()

    content['username'] = request.user.username
    content['token'] = user_obj.auth_token.key
    return HttpResponse(json.dumps(content), content_type='application/javascript;charset=utf-8')


def token_login(request):
    content = {'this': 'token_login', 'method': request.method}
    token_key = request.GET.get('token')

    try:
        token = Token.objects.get(key=token_key)
        content['Token_search'] = True
        try:
            user_obj = User.objects.get(id=token.user_id)
            content['User_search'] = True
            # 此处用的是authenticate接口方法， 该接口会查询settings中设定的backend，用匹配的方法实现鉴权
            user = authenticate(token=user_obj.auth_token.key)
            login(request, user)
        except User.DoesNotExist:
            content['User_search'] = False

    except Token.DoesNotExist:
        content['token_search'] = False

    return HttpResponse(json.dumps(content), content_type='application/javascript;charset=utf-8')