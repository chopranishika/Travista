from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^cafe/$', views.Cafe ,name = 'cafe'),
	url(r'^hospital/$', views.Hospital ,name = 'hospital'),
	url(r'^school/$', views.School ,name = 'school'),
	url(r'^malls/$', views.Shopping_mall ,name = 'shopping_mall'),
	url(r'^restaurant/$', views.Restaurant ,name = 'restaurant'),
	url(r'^theater/$', views.Movie_theater ,name = 'Movie_theater'),
	url(r'^(?P<id>[0-9]+)/$', views.detail ,name = 'detail'),
]
