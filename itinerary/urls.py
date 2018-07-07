from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^travel$', views.travel,name='travel'),
    url(r'^addplan$', views.addplan,name='addplan'),
    url(r'^createplan$', views.createplan,name='createplan'),
    url(r'^show/(?P<travel_id>\d+)$', views.show,name='show'),
    url(r'^join/(?P<travel_id>\d+)$', views.join,name='join'),
    url(r'^delete/(?P<id>\d+)$', views.delete,name='delete')
]
