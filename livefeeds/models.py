from __future__ import unicode_literals
from django.conf import settings 
from django.db import models

# Create your models here.

class livefeeds(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, blank= True ,null= True)
	place_name = models.CharField(max_length=120)
	image = models.FileField(null=True,blank=True)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=True,auto_now_add=False)
	lat = models.FloatField(blank=True, null=True)
	lng = models.FloatField(blank=True, null=True)
	
	
	def __unicode__(self):
		return self.place_name

	def __str__(self):
		return self.place_name	
		
	class Meta:
		ordering = ["-timestamp","-updated"]