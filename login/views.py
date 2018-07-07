from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from login.forms import SignUpForm,Contactus
from .models import contact


@login_required
def home(request):
		form1 = Contactus(request.POST)
		if form1.is_valid():
			instance = form1.save(commit=False)
			instance.user = request.user
			instance.save()
		#template = 'home.html'
		context = {"form1" : form1}
		#messages.success(request,"Feed Posted")
		
		return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



		