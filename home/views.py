from django.shortcuts import render
from .models import Entrance
from django.core import exceptions
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from .serializers import EntranceSerializer


# Create your views here.


def index(request):
    if request.method == 'GET':
        return render(request, 'home/index.html')
    if request.method == 'POST':
        app_name = request.POST.get('app_name').lower()
        try:
            ent = Entrance.objects.get(entrance=app_name)
        except exceptions.ObjectDoesNotExist:
            context = {"error": "Invalid Entrance {}".format(app_name)}
            return render(request, 'home/index.html', context)
        return redirect(ent.entrance_url)


def login_processor(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            return redirect("/")
        else:
            return redirect("/login_page")


def logout_processor(request):
    if request.user.is_authenticated():
        logout(request)
        return redirect("/")
    else:
        return redirect("/")


class EntranceViewSet(viewsets.ModelViewSet):
    queryset = Entrance.objects.all()
    serializer_class = EntranceSerializer







