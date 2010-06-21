from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from tamarindo.task.models import Task

def index(request):
    task_list = Task.objects.all()
    return render_to_response('index.html', {'task_list': task_list})

def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render_to_response('detail.html', {'task': task},
                               context_instance=RequestContext(request))
    