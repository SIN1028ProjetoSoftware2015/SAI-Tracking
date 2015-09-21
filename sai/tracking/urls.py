from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^map-in$', views.map_in, name='map_in'),
	url(r'^map-out$', views.map_out, name='map_out'),
]