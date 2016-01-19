# coding=utf-8
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from lib.jieba import jieba as wintercome
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

def wintercome_api(request):
    context = {}
    payload = "这里假设读者已经大致了解整个广告系统。而索引系统则提供一切业务的数据基础。DP的索引系统的主程序现在叫Lego（乐高）。Lego系统是非常先进的设计，这个索引系统不是普通关系数据库中的对表数据添加索引的概念，而是把整个数据库中和广告相关的希望用到的数据全部取出，生成全量数据索引文件给下游服务调用.\n依赖数据库的下游服务会使用Lego产生的全量数据索引文件去生成 全文索引 ，加载进内存。"

    words_list = wintercome.lcut(payload)  # 默认是精确模式
    context['words_list'] = words_list
    full_words_list = wintercome.lcut(payload, cut_all=True)
    context['full_words_list'] = full_words_list
    return HttpResponse(json.dumps(context), content_type='application/json')







