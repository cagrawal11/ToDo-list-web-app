from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def index_view(request):
	#return HttpResponse('hello world')
	return render_to_response("index.html")
