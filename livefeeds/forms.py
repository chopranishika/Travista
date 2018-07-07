from django import forms

from .models import livefeeds

class Createlivefeeds(forms.ModelForm):

    class Meta:
        model = livefeeds
        fields = ('place_name', 'content','image','lat','lng')