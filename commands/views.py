from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView

from commands.moduls import tasks

def index(request):

    result = ''
    task_number = request.GET.get('task_number')

    if task_number:    
        result = tasks.complete_task(task_number, request.GET.get('count_number'), request.GET.get('search_number'), 
                                                        request.GET.get('input_str'), request.GET.get('search_str'))

    context = {
        'result': result,
    }
 
 
    return render(request, 'commands/index.html', context)

