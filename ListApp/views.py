from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
#from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User
#from django.contrib import messages
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt



import models, datetime
# Create your views here.

def index_view(request):
	#return HttpResponse('hello world')
	return render_to_response("index.html", {'data1':': I m just learning now..', 'date': datetime.datetime.utcnow()})

@csrf_exempt
def add_task(request):
	#c = {}
	#c.update(csrf(request))
	#task_description = request.POST['taskToDo']if request.
	c = RequestContext(request)
	task = models.AddTask(TaskDescription = 'first task', TaskCreatedOn = datetime.datetime.now())
	task.save()
	return render("addTask.html", RequestContext(request))