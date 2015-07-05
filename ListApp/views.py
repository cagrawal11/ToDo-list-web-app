from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

import models, datetime
# Create your views here.

def index_view(request):
	#return HttpResponse('hello world')
	return render_to_response("index.html", {'data1':': I m just learning now..', 'date': datetime.datetime.utcnow()})


def add_task(request):
	task_description = request.POST['taskToDo']
	models.AddTask(TaskDecription = task_description)
	models.AddTask.save()
	return render_to_response("addTask.html")