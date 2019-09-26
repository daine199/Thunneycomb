#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json
import logging
from django.core import exceptions

from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse

from platycodon.models import Platycodon

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

def get_platycodon_by_id(request):
    res = {'title': None, 'content': None}
    platycodon_id = 0
    if request.method == 'GET':
        platycodon_id = request.GET.get('id')
        logger.info(platycodon_id)
    try:
        platycodon = Platycodon.objects.get(id=platycodon_id)
        res['title'] = platycodon.title
        res['content']: platycodon.content
    except exceptions.ObjectDoesNotExist:
        logger.warning("\nplatycodon not found.")

    return JsonResponse(res, safe=False)



