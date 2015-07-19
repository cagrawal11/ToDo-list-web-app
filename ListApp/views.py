from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
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
def sign_up(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		confirm_password = request.POST.get('confirm_password', False)
		if username == '' or password == '' or confirm_password == '':
			messages.error(request, "No field can be left empty")
			return render(request, "index.html", {})
		if password != confirm_password:
			#print "AG"
			messages.error(request, "passwords don't!!")
			return render(request, "index.html", {})
			#return HttpResponse("in 1st if")
		else:
			if User.objects.filter(username=username):
				messages.error(request,"User already exist")
				return render(request, "index.html", {'message': 'user exist'})
				#return HttpResponse("exiting user")
			else:
				user = User.objects.create_user(username=username, password=password)
				user.save()
				user = authenticate(username=username, password=password)
				login(request, user)
				return render(request, "index.html", {'user':user})

@csrf_exempt
def sign_in(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active():
				login(request, user)
				messages.success(request, "Login successfull")
				return render(request, "index.html",{'user':user})
			else:
				messages.error(request, "User is not active, account has been disabled!")
				return render(request, 'index.html', {})
		else:
			messages.error(request,"Username and password doesnot match!!")
			return request(request, 'index.html',{})


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


@csrf_exempt
def show_today(request):
	today_task = models.AddTask.objects.filter(TaskCreatedOn = datetime.datetime.today())
	context = {'all_task_list': all_task_list} #only 5 are passed now
	return render(request, 'show_all.html', context)
	

#@csrf_exempt
#def delete_task(render):
