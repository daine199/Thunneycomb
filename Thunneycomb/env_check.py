#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Daine.H

import os
import linecache


#  取环境设定。返回默认值dev或生产环境 product
def get_env(env='dev'):
    try:
        user_path = os.getenv('HOME')
        appenv = os.path.join(user_path, 'webapp/appenv')
        return linecache.getline(appenv, 1).lower().strip().split('=')[-1] or env
    except IOError:
        return env
