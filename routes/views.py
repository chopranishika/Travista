from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def routes(request) :
	if request.user.is_authenticated():
		template = 'routes.html'
		return render(request, template)
	else :
		return redirect('login')
	