from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def apt_test(request):
    print(request.method)
    content = {'this': 'Pet API Tests', 'method': request.method}
    return HttpResponse(json.dumps(content), content_type='application/javascript;charset=utf-8')
