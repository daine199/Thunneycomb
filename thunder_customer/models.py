#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
# Owner Daine.H
# Modify 2017-12-15
"""

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=17, blank=True)
    department = models.CharField(max_length=200, default='TestAddr', blank=True)

    def __str__(self):
        return self.user.username
