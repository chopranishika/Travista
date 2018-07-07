from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count
from .models import Travel , travelManager
from login.forms import SignUpForm,Contactus
from django.contrib.auth.models import User
#from .models import contact
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
# Create your views here.


def travel(request):
    if request.user.is_authenticated():
     current_user = request.user
     context = {
	"user": request.user.id,
	"travels" : Travel.objects.all(),
	"others": Travel.objects.all().exclude(join__id=request.user.id)
	}
     return render(request, 'travelplan.html', context)
    else :
     return redirect ("/")


def addplan(request):
    if request.user.is_authenticated():
     current_user = request.user
     context={"user":current_user
                 }
     return render(request, 'addplan.html', context)
        
    else:
     return redirect ("/")

def createplan(request):
    if request.method != 'POST':
        return redirect ("addplan")
    current_user = request.user
    newplan= Travel.objects.travelval(request.POST, request.user)
    if newplan[0] == True:
        return redirect('travel')
    else:
        for message in newplan[1]:
            messages.error(request, message)
        return redirect('addplan')

def show(request, travel_id):
    try:
        travel= Travel.objects.get(id=travel_id)
    except Travel.DoesNotExist:
        messages.info(request,"Travel Not Found")
        return redirect('travel')
    current_user = request.user
    context={
        "travel": travel,
        "user":current_user,
        "others": User.objects.filter(joiner__id=travel.id).exclude(id=travel.creator.id),
    }
    return render(request, 'showdetail.html', context)

def join(request, travel_id):
    if request.method == "GET":
        messages.error(request,"What trip?")
        return redirect('/')
    joiner= Travel.objects.join(request.user.id, travel_id)
    print (80 * ('*'), joiner)
    if 'errors' in joiner:
        messages.error(request, joiner['errors'])
    return redirect('travel')

#
def delete(request, id):
    try:
        target= Travel.objects.get(id=id)
    except Travel.DoesNotExist:
        messages.info(request,"Message Not Found")
        return redirect('/travel')
    target.delete()
    return redirect('/travel')
#
