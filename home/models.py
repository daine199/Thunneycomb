#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
# Owner Daine.H
# Modify 2016-11-23
"""
from django.db import models


class Entrance(models.Model):
    entrance = models.CharField(max_length=32)
    entrance_url = models.CharField(max_length=1024)

    class Meta:
        permissions = (
            ("view_entrance", "Can see entrance"),
        )

    def __str__(self):
        return self.entrance


class Switch(models.Model):
    switch_key = models.CharField(max_length=128)
    switch_value = models.BooleanField(default=False, verbose_name="Status")

    def __str__(self):
        return str(self.switch_value)
