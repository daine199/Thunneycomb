from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout

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



