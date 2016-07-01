from django.shortcuts import redirect
import time
import random

# Create your views here.


def performance_in(request, delay=None):
    if delay is None:
        delay = random.random() * 10
    else:
        delay = int(delay)
    print("sleep {0}s".format(delay))
    time.sleep(delay)
    return redirect("/")
