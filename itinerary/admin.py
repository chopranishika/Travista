from django.contrib import admin

# Register your models here.
from  itinerary.models import travelManager,Travel


class TravelModelAdmin(admin.ModelAdmin):
	list_display = ["destination","description","start","end","creator"]
	list_display_links = ["creator"]
	list_filter = ["creator"]
	search_fields = ["creator"]
	
	class Meta:
		model = Travel
		
admin.site.register(Travel,TravelModelAdmin)		