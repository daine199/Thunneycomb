#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Daine.H
import requests
from django.conf import settings
import json
from .commonLib import generate_verification_code
from ..models import MySubMail, SmsSender
from django.core.exceptions import ObjectDoesNotExist
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def send_code_sms(phone_no,
                  code_length=settings.DEFAULT_CODE_LENGTH,
                  valid_time=settings.DEFAULT_VALID_TIME,
                  sender_name=None):
    """

    :param phone_no: 目标电话号码
    :param code_length: 默认6，验证码长度
    :param valid_time:  默认120s， 验证码时效
    :param sender_name:  默认找None， 发送器名
    :return:
    """
    sender = get_sms_sender(sender_name)
    if settings.INVALID_SENDER is sender:
        logger.warning('No sender inited, send Failed.')
        return False
    else:
        gen_sms_obj(phone_no=phone_no,
                    code_length=code_length,
                    valid_time=valid_time,
                    sender=sender)


def gen_sms_obj(phone_no, code_length, valid_time, sender):
    """

    :param phone_no: 发送目标
    :param code_length: 验证码长度， 默认6
    :param valid_time: 有效时间，默认120s
    :param sender: 发送器对象
    :return:
    """
    code = generate_verification_code(code_length)
    sender_body = assemble_sender_body(sender, phone_no, code, valid_time)
    sms_send = requests.post(sender.sender_url, json=sender_body, headers=settings.SMS_HEADER)
    if is_send_success(json.loads(sms_send.text)):
        code_status = True
    else:
        code_status = False
    sms_obj = MySubMail(phone_no=phone_no,
                        code=code,
                        valid_time=valid_time,
                        code_status=code_status,
                        sender_name=sender)
    sms_obj.save()

    return sms_obj


def is_send_success(send_res):
    if 'success' == send_res['status']:
        logger.info("send sms success.")
        return True
    else:
        logger.warning("send sms Failed")
        logger.info(send_res)
        return False


def assemble_sender_body(sender, phone_no, code, valid_time):
    body_vars = json.loads(sender.template)
    body_vars['code'] = code
    body_vars['time'] = valid_time
    sender_body = {"appid": sender.app_id,
                   "project": sender.template_id,
                   "signature": sender.secret,
                   "vars": body_vars,
                   'to': phone_no}
    logger.info('sender body {}'.format(sender_body))
    return sender_body


def get_sms_sender(sender_name=None):
    """
    获取发送器
    :param sender_name:字符串发送器名
    :return: 发送器对象或 __INVALID_SENDER
    """
    sender = settings.INVALID_SENDER
    if None is sender_name:
        try:
            sender = SmsSender.objects.get(id=1)
        except ObjectDoesNotExist:
            logger.warning("Sender id=1 not found.")
    else:
        try:
            sender = SmsSender.objects.get(sender_name=sender_name)
        except ObjectDoesNotExist:
            logger.warning("Sender {} not found.".format(sender_name))
    return sender


def init_default_sender():
    try:
        sender = SmsSender.objects.get(id=1)
        logger.warning("init sender to default value.")
    except ObjectDoesNotExist:
        logger.warning("sender init passivity.")
        sender = SmsSender(sender_name=settings.SMS_SENDER['sender_name'],
                           sender_url=settings.SMS_MAIN_URL,
                           app_id=settings.SMS_SENDER['appid'],
                           secret=settings.SMS_SENDER['signature'],
                           template_id=settings.SMS_SENDER['project'],
                           template=settings.SMS_SENDER['vars'])
        sender.id = 1

    sender.sender_name = settings.SMS_SENDER['sender_name']
    sender.sender_url = settings.SMS_MAIN_URL
    sender.app_id = settings.SMS_SENDER['appid']
    sender.secret = settings.SMS_SENDER['signature']
    sender.template_id = settings.SMS_SENDER['project']
    sender.template = settings.SMS_SENDER['vars']

    sender.save()

