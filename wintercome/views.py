from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import cmdTask, runLevel, winterUser
import json, time

#
# def basic_cmd_run(request):
#     pass

# def basic_cmd_run(request, cmd_id):
#     ret = cmdTask.objects.get(id=int(cmd_id)).baseCall()
#     res = json.dumps(ret)
#     return HttpResponse(res)
#     # return HttpResponse('Return code: {0} \n{1}'.format(resprint))
#     #return HttpResponse("You're looking at cmd {0}.".format(cmd_id))

def basic_cmd_run(request,cmd_id):
    context = {}
    cmdtask = cmdTask.objects.get(id=int(cmd_id))
    res = cmdtask.baseCall()
    context['task'] = cmdtask
    context['code'] = res['returncode']
    context['result'] = res['returnprint']
    return render(request, 'wintercome/runresult.html', context)


def cmd_index_page_limit(request):
    # time.sleep(5000000)
    i = 0
    while i <= 999999:
        i += 1
        print("sleeping")
    context = {}
    cmdtasklist = cmdTask.objects.all()
    context['cmdtasklist'] = cmdtasklist
    print("sleep 500000")
    return render(request, 'wintercome/cmdlist.html', context)

def cmd_index_page(request):
    context = {}
    cmdtasklist = cmdTask.objects.all()
    context['cmdtasklist'] = cmdtasklist
    return render(request, 'wintercome/cmdlist.html',context)