from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    access_entry = ("login", "logout")
    ext_entry = ("requests", "django")
    if request.method == 'GET':
        return render(request, 'home/index.html')
    if request.method == 'POST':
        app_name = request.POST.get('app_name').lower()

        if app_name in access_entry:
            return redirect("/" + app_name)

        elif app_name in ext_entry:
            if app_name == "requests":
                return redirect("http://www.python-requests.org/en/master/")

        elif app_name in settings.INSTALLED_APPS:
            return redirect("/" + app_name)

        elif app_name == "admin":
            if request.user.is_authenticated():
                return redirect("/" + app_name)
            else:
                return render(request, 'home/index.html')

        else:
            context = {"error": "Invalid App"}
            return render(request, 'home/index.html', context)


@login_required(login_url='/login/')
def login_test_page(request):
    return HttpResponse("test")


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


def login_page(request):
    if request.method == 'GET':
        print(request.path)
        if not request.user.is_authenticated():
            return render(request, 'home/login.html')
    else:
        userid = request.POST.get('userid')
        password = request.POST.get('password')
        print(userid, password)
        user = authenticate(username=userid, password=password)
        if user is not None:
            login(request, user)
            return redirect('/wiki')
        else:
            return redirect("/")

