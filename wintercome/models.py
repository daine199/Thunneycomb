from __future__ import unicode_literals

from django.db import models

# Create your models here.
import base64, time, subprocess, shlex


# Owner Daine.H
# Modify 2016-01-04

class CmdTask(models.Model):
    title = models.CharField(max_length=32)
    userid = models.IntegerField(default=1)
