from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    access_entry = ("login", "logout", "wiki", "admin", "php")
    ext_entry = ("requests", "django")
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

        elif app_name in ext_entry:
            if app_name == "requests":
                return redirect("http://www.python-requests.org/en/master/")
            if app_name == "php":
                return redirect("http://www.thunneycomb.com:8000/")

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


# @login_required(login_url='/accounts/login/')
# def my_view(request):
#     return redirect("/wiki")




