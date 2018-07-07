from __future__ import unicode_literals
from django.conf import settings 
from django.db import models

# Create your models here.
class contact(models.Model):
	name = models.CharField(max_length=120)
	email = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	message = models.TextField()
	
	
	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name	