from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserChangeForm ,PasswordChangeForm
from django.contrib.auth.models import User
from myprofile.forms import EditProfileForm
from django.conf import settings





def view_profile(request):
	if request.user.is_authenticated():
		context = {'user':request.user}
		return render(request, 'myprofile.html',context)
	else :
		return redirect('login')


def edit_profile(request):
        if request.method == 'POST':
                form = EditProfileForm(request.POST,instance=request.user)
                if form.is_valid():
                        form.save()
                        return render(request,'editprofile.html',{'form': form})
        else:
                form = EditProfileForm(instance=request.user)
        return render(request,'editprofile.html',{'form': form})

def changepassword(request):
        if request.method == 'POST':
                form=PasswordChangeForm(data=request.POST,user=request.user)
                if form.is_valid():
                        form.save()
                        return render(request, 'editprofile.html', {'form': form})

        else:
                form = PasswordChangeForm(user=request.user)
        return render(request,'editprofile.html',{'form': form})


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request,'editprofile.html',{'form': form})

