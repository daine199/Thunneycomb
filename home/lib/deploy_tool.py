#! /usr/bin/env python
# -*- coding: utf-8 -*-
import shlex

import copy
import subprocess

import time


def deploy_perms_static():
    """

    :return:  返回固定的权限
    """
    #  TODO 在之后需要能够传入参数，修正一些特殊权限
    deploy_perms_entry = ('sites.change_site', 'sites.add_site')
    return copy.deepcopy(deploy_perms_entry)


def check_deploy_perms(user):
    """

    :param user:  Model User Object
    :return:  bool deploy access perms.
    """
    #  TODO 在之后Thunneyconmb如果添加了权限管理APP，则可以替换相应权限需求。目前部署暂时用sites替代。
    permission_required = deploy_perms_static()
    deploy_perms = user.has_perms(permission_required)
    return deploy_perms


def deploy_app(app_name='thunneycomb', version=None):
    now = time.localtime()
    ver_format = time.strftime("%Y.%m.%d_%H.%M", now)

    if 'thunneycomb' == app_name.lower():
        if version is None:
            version = 'AutoDeploy.{0}'.format(ver_format)
        else:
            version = '{0}.{1}'.format(version, ver_format)
        cmd = "deploy.sh {0}".format(version)
        subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
        report_out = "{0} Deploying...".format(version)

    if 'weimo' == app_name.lower():
        if version is None:
            version = 'Weimo_AutoDeploy.{0}'.format(ver_format)
        else:
            version = '{0}.{1}'.format(version, ver_format)
        cmd = "bash /home/sophie.mao/bin/deploy.sh {0}".format(version)
        subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
        report_out = "{0} Deploying...".format(version)

    else:
        report_out = "{0} AutoDeploy unavailable. ".format(app_name)

    return report_out





