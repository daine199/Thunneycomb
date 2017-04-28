from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def apt_test(request):
    request_method = request.method
    content = {'this': 'Pet API Tests', 'method': request_method}
    if 'POST' == request_method:
        print("In Create")
    if 'GET' == request_method:
        print("In Retrieve")
    if 'PUT' == request_method or 'PATCH' == request_method:
        print("In PUT/PATCH")
    if 'DELETE' == request_method:
        print("In DELETE")
    return HttpResponse(json.dumps(content), content_type='application/javascript;charset=utf-8')
