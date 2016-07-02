from django.db import models
from django.contrib.auth.models import User
from redactor.fields import RedactorField

import datetime
import re

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name="标题")
    content = RedactorField(verbose_name="内容")
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title


