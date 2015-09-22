from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # Mapas
    url(r'^map-in$', views.map_in, name='map_in'),
    url(r'^map-out$', views.map_out, name='map_out'),
    # Formularios
    url(r'^form-in$', views.form_in, name='form_in'),
	url(r'^form-out$', views.form_out, name='form_out'),
]