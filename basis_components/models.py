#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Daine.H

from django.db import models
import logging
import time
# Create your models here.

# Get an instance of a logger
logger = logging.getLogger(__name__)


class MySubMail(models.Model):
    phone_no = models.CharField(max_length=18)
    code = models.CharField(max_length=6)
    sms_body = models.CharField(max_length=256, blank=True)
    gen_time = models.FloatField(default=time.time, auto_created=True)
    valid_time = models.CharField(max_length=128, default='120')
    code_status = models.BooleanField(default=True)
    sender_name = models.CharField(max_length=18, blank=True)

    def get_code_valid(self, code=None):
        """
        校验验证码，调用后验证码无论是否正确都会直接失效。
        :return: Bool 校验结果
        """
        self.set_invalid_status()
        check_status = False

        # 校验时效
        if (time.time() - self.gen_time) <= float(self.valid_time):
            logger.info('验证码未过期')
            # 校验验证码输入
            if code == self.code:
                logger.info('验证码一致')
                check_status = True
            else:
                check_status = False
        else:
            check_status = False
        return check_status

    def set_invalid_status(self):
        self.code_status = False
        self.save()

    def __str__(self):
        return self.phone_no


class SmsSender(models.Model):
    sender_name = models.CharField(max_length=18, unique=True, db_index=True)
    sender_url = models.CharField(max_length=256)
    app_id = models.CharField(max_length=128)
    secret = models.CharField(max_length=256)
    template_id = models.CharField(max_length=64)
    template = models.CharField(max_length=256)

    def __str__(self):
        return self.sender_name


