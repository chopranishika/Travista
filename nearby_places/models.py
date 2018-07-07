from django.db import models

class explore(models.Model):
	
	name = models.CharField(max_length=250)
	rating = models.FloatField(blank=True, null=True)
	vicinity = models.CharField(max_length=1000)
	type = models.CharField(max_length=25)
	lat = models.FloatField(blank=True, null=True)
	lng = models.FloatField(blank=True, null=True)
