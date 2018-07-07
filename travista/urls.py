from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main/', include('main.urls')),
	url(r'^login/', include('login.urls')),
	url(r'^myprofile/', include('myprofile.urls')),
	url(r'^flight/', include('flight.urls')),
	url(r'^bestdeals/', include('bestdeals.urls')),
	url(r'^livefeeds/', include('livefeeds.urls')),
	url(r'^nearby_places/', include('nearby_places.urls')),
	url(r'^routes/', include('routes.urls')),
	url(r'^itinerary/', include('itinerary.urls')),

]

if settings.DEBUG :
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)