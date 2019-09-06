#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json
import logging

from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse

from platycodon.models import Platycodon

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

def get_platycodon_by_id(request):
    platycodon_id = 0
    if request.method == 'GET':
        platycodon_id = request.GET.get('id')
        logger.info(platycodon_id)
    platycodon = Platycodon.objects.filter(id=platycodon_id)

    # print(serialize('json', platycodon))

    # class JsonResponse(data, encoder=DjangoJSONEncoder, safe=True, json_dumps_params=None, **kwargs)
    return JsonResponse(serialize("json", platycodon), safe=False)



