from django.contrib.auth.decorators import login_required
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
    access_entry = ("login", "logout", "wiki", "admin")
    if request.method == 'GET':
        return render(request, 'home/index.html')
    if request.method == 'POST':
        app_name = request.POST.get('app_name').lower()

        if app_name in access_entry:
            if app_name == "login":
                return redirect('/admin/login/?next=/')
            if app_name == "wiki":
                return redirect('/admin/login/?next=/wiki')
            return redirect("/" + app_name)

        if app_name == "admin":
            if request.user.is_authenticated():
                return redirect("/" + app_name)
            else:
                return render(request, 'home/index.html')

        else:
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


@login_required
class EntranceViewSet(viewsets.ModelViewSet):
    queryset = Entrance.objects.all()
    serializer_class = EntranceSerializer


@csrf_exempt
def entrance_list(request):
    """
    List all code entrance, or create a new entrance.
    :param request:
    """
    if request.method == 'GET':
        entrance = Entrance.objects.all()
        serializer = EntranceSerializer(entrance, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EntranceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def entrance_detail(request, pk):
    """
    Retrieve, update or delete a code entrance.
    :param pk:
    :param request:
    """
    try:
        entrance = Entrance.objects.get(pk=pk)
    except Entrance.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'DELETE':
        entrance.delete()
        return HttpResponse(status=204)

    if request.method == 'GET':
        serializer = EntranceSerializer(entrance)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EntranceSerializer(entrance, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)




