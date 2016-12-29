#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
# Owner Daine.H
# Modify 2016-11-23
"""
from django.db import models
from django.contrib.auth.models import User, Permission


class Entrance(models.Model):
    entrance = models.CharField(max_length=32)
    entrance_url = models.CharField(max_length=1024)

    class Meta:
        permissions = (
            ("can_view", "Can see available entrance"),
            ("can_add", "Can add a entrance"),
            ("can_change", "Can change a entrance"),
            ("can_del", "Can remove a entrance"),
        )

    def __str__(self):
        return self.entrance


class EntrancePermission(models.Model):
    user = models.ForeignKey(User)
    has_index_perm = models.BooleanField()


