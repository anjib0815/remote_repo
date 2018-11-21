from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def dateinfo(request):
	date=datetime.datetime.now()
	msg='<h1>Hi Good Morning</h1><hr>'
	msg=msg+'<h1> The curent time is:'+ str(date)+'</h1>'
	return HttpResponse(msg)