from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.


def login_page(request):
    context = {}
    if not request.user.is_authenticated():
        for key in request.POST:
            print(key)
        # username = request.POST['username']
        # password = request.POST['password']
        # print(username, password)
        return render(request, 'wintercome/login.html')
    #     user = authenticate(username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return render(request, 'wintercome/login.html')
    #     else:
    #         return render(request, 'wintercome/login.html')
    # else:
    #     return render(request, 'wintercome/login.html')
    #
