from django.conf.urls import url
from . import views 


urlpatterns = [
   
	url(r'^$', views.view_profile, name='view_profile'),
    url(r'^edit/$',views.edit_profile, name='edit_profile'),
	url(r'^password/$',views.changepassword, name='changepassword'),
]
