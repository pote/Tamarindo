from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from tamarindo.task.models import Task

def index(request):
    task_list = Task.objects.all()
    return render_to_response('index.html', {'task_list': task_list})

