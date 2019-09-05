#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Daine.H

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def my_view(request):
    logger.error('Something went wrong!')
    logger.debug('debug out put')
    logger.warning('warning out put')
    logger.error('error out put')
    logger.critical('critical')

