#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Daine.H
from django.contrib.auth.models import User


class TokenLoginBackend(object):
    @staticmethod
    def authenticate(token=None):
        if not token:
            return None
        else:
            try:
                user_obj = User.objects.get(auth_token=token)
            except User.DoesNotExist:
                return False
            user_obj.backend = 'home.lib.token_lib.TokenLoginBackend'
            return user_obj






