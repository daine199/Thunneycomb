from __future__ import unicode_literals

from django.db import models
from .lib import MACRO
# Create your models here.
import base64, time, subprocess, shlex


# Owner Daine.H
# Modify 2016-01-04

class CmdTask(models.Model):
    title = models.CharField(max_length=32)
    ownerid = models.CharField(max_length=32)
    cmd = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    run_level = models.IntegerField(blank=True)

    def __str__(self):
        return self.title


class RunLevel(models.Model):
    userid = models.CharField(max_length=32)
    level = models.IntegerField(default=MACRO.MENBER)

    def __str__(self):
        return self.title



