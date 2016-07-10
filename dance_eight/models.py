from django.db import models
from django.contrib.auth.models import User
from redactor.fields import RedactorField

import datetime
import re

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name="标题")
    author = models.ForeignKey(User)
    content = RedactorField(verbose_name="内容")
    pub_date = models.DateTimeField('发布日期')

    def __str__(self):
        return self.title


class Comment(models.Model):
    target = models.ForeignKey(Article)
    content = RedactorField(verbose_name="评论内容")

    def __str__(self):
        return self.target.title

