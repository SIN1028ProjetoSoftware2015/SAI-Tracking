from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # Mapas
    url(r'^map-in$', views.map_in, name='map_in'),
    url(r'^map-out$', views.map_out, name='map_out'),
    # Formularios
    url(r'^form-in$', views.form_in, name='form_in'),
    url(r'^form-in-contato$', views.form_in_contato, name='form_in_contato'),
    url(r'^form-in-instituicao$', views.form_in_instituicao, name='form_in_instituicao'),
	url(r'^form-out$', views.form_out, name='form_out'),
	# login
	url(r'^login', views.user_login, name='user_login'),
	# url(r'^logout', views.user_logout, name='user_logout'),
]