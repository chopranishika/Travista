from django.contrib import admin

# Register your models here.
from  livefeeds.models import livefeeds

class livefeedsModelAdmin(admin.ModelAdmin):
	list_display = ["place_name","updated","timestamp"]
	list_display_links = ["updated"]
	list_filter = ["updated","timestamp"]
	search_fields = ["place_name"]
	
	class Meta:
		model = livefeeds

admin.site.register(livefeeds,livefeedsModelAdmin)