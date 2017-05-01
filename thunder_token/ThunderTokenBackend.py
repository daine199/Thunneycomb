#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Daine.H

from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from rest_framework.authtoken.models import Token


class TokenBackend(ModelBackend):
    """
    # 1.继承 django.contrib.auth.backends.ModelBackend
    # 2.在settings中加入：
    AUTHENTICATION_BACKENDS = ('thunder_token（应用名）.ThunderTokenBackend（文件名）.TokenBackend（类名）',
                           'django.contrib.auth.backends.ModelBackend'
                           )
    # 3.在INSTALLED_APPS 中加入本应用
    """
    def authenticate(self, token=None, **kwargs):
        try:
            token_obj = Token.objects.get(key=token)

            try:
                user_obj = User.objects.get(id=token_obj.user_id)
                return user_obj
            except User.DoesNotExist:
                return None
        except Token.DoesNotExist:
            return None
