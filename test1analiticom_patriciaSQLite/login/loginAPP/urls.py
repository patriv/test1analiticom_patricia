from django.conf.urls import url
from . import views
from loginAPP.views import *


urlpatterns = [
	url(r'^$',
	Index.as_view(),
	name='index'),

	url(r'^register/$',
	Register.as_view(),
	name='register'),

	url(r'^home/$',
	Home.as_view(),
	name='home'),

	url(r'^restart/$',
	RestartPass.as_view(),
	name='restart'),

	url(r'^new-passw/$',
	NewPassw.as_view(),
	name='new_passw'),



]
