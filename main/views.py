from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect


def index(request) :
	if request.user.is_authenticated():
		return redirect('home')
	else :
		template = 'index.html'
		return render(request, template)
	