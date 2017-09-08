# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from home.models import index 
from django.contrib.auth.models import User

# Create your views here.
def indexs(request):
	Data = {
		'indexs':index.objects.all()
	}
	return render(request,'page/index.html',Data)

def contact(request):
	return render(request,'page/contact.html')
def info(request) :
	return render(request,'page/info.html')
def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(username = form.cleaned_data['username'],email = form.cleaned_data['email'],password = form.cleaned_data['password1'])
			return HttpResponseRedirect('/')
		return render(request,'page/register.html',{'form':form})
	form = RegistrationForm()
	return render(request,'page/register.html',{'form':form})		
