from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import User
from .models import Document

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name','email','username','password']
		

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )
		