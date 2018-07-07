from django.contrib import admin

# Register your models here.
from login.models import contact


class contactModelAdmin(admin.ModelAdmin):
	list_display = ["name","email","subject"]
	list_display_links = ["name"]
	list_filter = ["name"]
	search_fields = ["name"]
	
	class Meta:
		model = contact
		

admin.site.register(contact,contactModelAdmin)		