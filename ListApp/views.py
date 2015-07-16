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
	if request.method == "POST":
		c = RequestContext(request)
		abc = request.POST['taskToDo']
		tasktext = models.AddTask(TaskDescription = abc, TaskCreatedOn = datetime.datetime.now())
		tasktext.save()
		'''add message pop-up "Task Added successfully" '''
		return render(request,"index.html",{})

@csrf_exempt
def show_all(request):
	all_task_list = models.AddTask.objects.all()
	context = {'all_task_list': all_task_list} #only 5 are passed now
	return render(request, 'show_all.html', context)