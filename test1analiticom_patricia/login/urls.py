from django.conf.urls import url,patterns
from . import views
from login.views import *

urlpatterns = patterns('',
    url(r'^$',
    Index.as_view(),
     name='index'),

     url(r'^login/$',
     'login.views.user_login',
      name='login'),

     url(r'^register/$',
     Register.as_view(),
      name='register'),

     url(r'^home/$',
        Home.as_view(),
        name='home')
 )
