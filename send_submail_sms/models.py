from django.db import models
from django.conf import settings
import logging
import requests
import json
import datetime
# Create your models here.

# Get an instance of a logger
logger = logging.getLogger(__name__)


class MySubMail(object):
    pass


class Sender(object):

    # Sender information
    _appid = None
    _project = None
    _signature = None
    _body_vars = None
    _url = "https://api.mysubmail.com/message/xsend"
    _bak_url = None
    _header = None

    _sender_body = {}
    _status = None

    def __init__(self, default_sms_sender=None):
        if None is default_sms_sender:
            try:
                self._sms_sender = settings.SMS_SENDER
                self._status = True
                self._appid = self._sms_sender['appid']
                self._project = self._sms_sender['project']
                self._signature = self._sms_sender['signature']
                self._body_vars = self._sms_sender['vars']
            except AttributeError:
                logger.warning(ArithmeticError)
                logger.info("Get SMS_SENDER template Failed, Need init manually.")
                self._sms_sender = {}
                self._status = False
            try:
                self._url = settings.SMS_MAIN_URL
                self._header = settings.SMS_HEADER
            except AttributeError:
                logger.warning(ArithmeticError)
                logger.info("Get SMS_URL Failed, Need init manually.")
                self._status = False
        else:
            self._sms_sender = default_sms_sender

        print(self.get_sender_info())

    def is_sender_ready(self):
        if True is self._status:
            logger.info("sms sender ready.")
            return True
        else:
            logger.warning("sms sender not ready.")
            return False

    @property
    def appid(self):
        logger.info("Get appid value")
        return self._appid

    @appid.setter
    def appid(self, appid):
        logger.info("Set appid value = {}".format(appid))
        self._appid = appid

    @property
    def project(self):
        logger.info("Get project value")
        return self._project

    @project.setter
    def project(self, project):
        logger.info("Set project value = {}".format(project))
        self._project = project

    @property
    def signature(self):
        logger.info("Get signature value")
        return self._signature

    @signature.setter
    def signature(self, signature):
        logger.info("Set signature value = {}".format(signature))
        self._signature = signature

    @property
    def url(self):
        logger.info("Get url value")
        return self._url

    @url.setter
    def url(self, url):
        logger.info("Set url value = {}".format(url))
        self._url = url

    @property
    def header(self):
        logger.info("Get header value")
        return self._header

    @header.setter
    def header(self, header):
        logger.info("Set header value = {}".format(header))
        self._header = header

    @property
    def body_vars(self):
        logger.info("Get body_vars value")
        return self._body_vars

    @body_vars.setter
    def body_vars(self, body_vars):
        logger.info("Set body_vars value = {}".format(body_vars))
        self._body_vars = body_vars

    @property
    def sender_info(self):
        return self.get_sender_info()

    def get_sender_info(self):
        sender_info = {'status': self._status,
                       'appid': self._appid,
                       'project': self._project,
                       'signature': self._signature,
                       'sms_url': self._url,
                       'sms_url_bak': self._bak_url}
        return sender_info

    @property
    def sender_body(self):
        sender_body = {"appid": self._appid,
                       "project": self._project,
                       "signature": self._signature}
        self._sender_body = sender_body
        logger.info("Get Sender body Value.")
        return self._sender_body

    def sender_status_check(self):
        body = self.sender_body
        body['to'] = '18601676833'
        body['vars'] = {'code': '123456', 'time': '120'}
        sender = requests.post(self.url, json=body, headers=self.header)
        res = json.loads(sender.text)
        logger.info(res)

        if res['status'] == "success":
            self._status = True
            logger.info("Sender is ready.")
            logger.info(self.sender_info)
        else:

            logger.warning("Sender not ready")
            logger.info(self.sender_info)
            self._status = False

        logger.info(self.sender_info)
        return self._status

    def sender_sms(self, phone_no=None, code=None, time=None):
        now_time = datetime.datetime.now().strftime(settings.NOW_STRFTIME)
        send_log = {"to": phone_no,
                    "code": code,
                    "time": time,
                    "send_time": now_time}

        if None is phone_no:
            logger.warning("Phone No wrong. {}".format(phone_no))
            self._status = False
        elif None is code:
            logger.warning("Code No wrong. {}".format(code))
            send_status = False
        elif None is time:
            logger.warning("Time No wrong. {}".format(time))
            send_status = False
        else:
            vars_body = {"code": code, "time": time}
            body = self.sender_body
            body['vars'] = vars_body
            body['to'] = phone_no
            sender = requests.post(self.url, json=body, headers=self.header)
            res = json.loads(sender.text)
            logger.info(res)

            if res['status'] == "success":
                send_status = True
                logger.info("Success send sms to {}.".format(phone_no))
                logger.info(self.sender_info)
            else:
                logger.warning("Send Failed.")
                logger.info(self.sender_info)
                send_status = False

        send_log['status'] = send_status
        return send_log

