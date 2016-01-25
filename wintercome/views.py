# coding=utf-8
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
import jieba
from jieba import posseg
import json
from django.views.decorators.csrf import csrf_exempt

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


def wintercome_test(request):
    context = {}
    words_dic_list = []
    payload = "这里假设读者已经大致了解整个广告系统。而索引系统则提供一切业务的数据基础。DP的索引系统的主程序现在叫Lego（乐高）。Lego系统是非常先进的设计，这个索引系统不是普通关系数据库中的对表数据添加索引的概念，而是把整个数据库中和广告相关的希望用到的数据全部取出，生成全量数据索引文件给下游服务调用.\n依赖数据库的下游服务会使用Lego产生的全量数据索引文件去生成 全文索引 ，加载进内存。"

    #words_list = wintercome.cut(payload)  # 默认是精确模式
    words_list = posseg.cut(payload)
    for w in words_list:
        words_dic_list += [{"word":w.word,"flag":w.flag}]
    context['words_dic_list'] = words_dic_list
    return HttpResponse(json.dumps(context),
                        content_type='application/json')


@csrf_exempt
def wintercome_api(request):
    """
    :param request: 使用POST传入表单,内容为payload
    :return: 返回json字符串{'words_list':[],'full_words_list':[]}
    """
    context = {}
    words_list = []
    full_words_list = []
    payload = request.POST.get('payload')
    print("This is payload\n", payload)
    words_list_obj = jieba.cut(payload)  # 默认是精确模式
    for w in words_list_obj:
        words_list += [w]
    context['words_list'] = words_list
    full_words_obj = jieba.cut(payload, cut_all=True)
    for w in full_words_obj:
        full_words_list += [w]
    context['full_words_list'] = full_words_list
    return HttpResponse(json.dumps(context),
                        content_type='application/json')








