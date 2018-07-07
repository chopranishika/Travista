from django.contrib import admin
from nearby_places.models import explore


class exploreModelAdmin(admin.ModelAdmin):
	list_display = ["name","type","lat","lng"]
	list_display_links = ["name"]
	list_filter = ["type"]
	search_fields = ["type"]
	
	class Meta:
		model = explore

admin.site.register(explore,exploreModelAdmin)

admin.site.site_header = 'Travista Admin'
admin.site.site_title = 'Travista Admin'