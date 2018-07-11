#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Daine.H


# Send mail start
BASE_COMPONENTS = ['basis_components']

SMS_SENDER = {"sender_name": "mysubmail",
              "appid": "18253",
              "to": "18601676833",
              "project": "YoYXG",
              "signature": "32263cb96de29b7ad167b7b10e00197b",
              "vars": '{"code": "123abc", "time": "120"}'}

SMS_MAIN_URL = 'https://api.mysubmail.com/message/xsend'
SMS_BACKUP_URL = 'https://api.submail.cn/message/xsend'
SMS_HEADER = {"Content-Type": "application/json"}

INVALID_SENDER = 'invalid_sender'
DEFAULT_VALID_TIME = '120'
DEFAULT_CODE_LENGTH = 6
# Send mail end
