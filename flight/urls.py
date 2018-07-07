from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$',views.flight,name = 'flight'),
	url(r'^detail/$',views.detail,name = 'detail'),
	
]