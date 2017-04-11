from django.conf.urls import url
from . import views
from loginAPP.views import *
from django.contrib.auth import views as auth_views


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

	url(r'^logout/$',
	auth_views.logout,
    {
        'next_page': '/'
    },
	name='logout'),

	url(r'^restart/$',
	RestartPass.as_view(),
	name='restart'),

	url(r'^new-passw/(?P<id>\w+)$',
	NewPassw.as_view(),
	name='new_passw'),

]
