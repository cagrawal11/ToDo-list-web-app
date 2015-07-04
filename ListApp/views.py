from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def index_view(request):
    '''First page of our app. This form just renders the first page, where one
    can register, or log in.'''
    if request.method == 'GET':
        return render_request('/index.html') 
