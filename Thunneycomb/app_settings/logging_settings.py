#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Daine.H
import os

# 在settings中导入该配置
# 该配置会覆盖django默认logger

THUNNEYCOMB_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s \n'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logs/debug.log',
            'formatter': 'verbose',
        },
        'warning': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': 'logs/warning.log',
            'formatter': 'verbose',
        },
        'trace': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/trace.log',
            'formatter': 'verbose',
        },
        'error': {
            'level': "ERROR",
            'class': 'logging.FileHandler',
            'filename': 'logs/error.log',
            'formatter': 'verbose',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'home': {
            'handlers': ['trace', 'error', 'console', 'warning'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': True,
        },
        'platycodon': {
            'handlers': ['trace', 'error', 'console', 'warning'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': True,
        },
    },
}

NOW_STRFTIME = '%Y-%m-%d %H:%M:%S'
