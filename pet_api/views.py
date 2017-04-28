from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.


def pet_get(request):
    if request.method == 'GET':
        content = {'this': 'Pet API GET Tests', 'method': request.method}
    return HttpResponse(json.dumps(content), content_type='application/javascript;charset=utf-8')
