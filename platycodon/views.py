#! /usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from django.core import exceptions
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required, login_required

from platycodon.models import Platycodon

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

@login_required()
@permission_required("platycodon.view_platycodon", raise_exception=True)
def get_platycodon_by_id(request):
    res = {'title': None, 'content': None}
    platycodon_id = 0
    if request.method == 'GET':
        platycodon_id = request.GET.get('id')
        logger.info(platycodon_id)
    try:
        platycodon = Platycodon.objects.get(id=platycodon_id)
        res['title'] = platycodon.title
        res['content'] = platycodon.content
    except exceptions.ObjectDoesNotExist:
        logger.warning("\nplatycodon not found.")

    return JsonResponse(res, safe=False)



