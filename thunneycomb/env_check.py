#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Daine.H

import linecache


#  取环境设定。返回默认值dev或生产环境 product
def get_env(env='dev'):
    try:
        return linecache.getline('~/webapps/appenv', 1).lower().strip().split('=')[-1] or env
    except IOError:
        return env
