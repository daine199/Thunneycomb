from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
import json

# Create your views here.


def login_page(request):
    context = {}
    if not request.user.is_authenticated():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(username, password, user)
        if user is not None:
            login(request, user)
        else:
            print("login failed.")
        # print(username, password)
    return render(request, 'wintercome/login.html')


def logout_page(request):
    logout(request)
    return render(request, 'wintercome/login.html')


def json_page(request):
    context = {'user': 'Daine.H', 'cmd': "ls -l", 'level': 100}
    return HttpResponse(json.dumps(context), content_type='application/json')



