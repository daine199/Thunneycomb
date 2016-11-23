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

    def __str__(self):
        return self.entrance


