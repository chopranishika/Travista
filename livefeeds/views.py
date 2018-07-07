from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .forms import Createlivefeeds
from .models import livefeeds
from contextlib import closing

def createfeeds(request):
	if request.user.is_authenticated():
		form = Createlivefeeds(request.POST or None,request.FILES or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
		template = 'postfeeds.html'
		context = {"form" : form}
		#messages.success(request,"Feed Posted")
		return render(request,template,context)
	else :
		return redirect('login')	
		
def viewfeeds(request):
	if request.user.is_authenticated():
		feed_list = livefeeds.objects.all()
		paginator = Paginator(feed_list, 15) # Show 25 contacts per page
		page = request.GET.get('page')
		try:feed=paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page.
			feed = paginator.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			feed = paginator.page(paginator.num_pages)
		template = 'livefeeds.html'
		context = {"object_list" : feed,
			   "place_name" : "List",
		}
		return render(request,template,context)
	else :
		return redirect('login')	
	
#def deletefeeds(request,id = None):
#		instance = get_object_or_404(livefeeds,id=id)
#		instance.delete()
#		return redirect('viewfeeds')
