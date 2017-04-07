#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import *
from django.template import RequestContext
from django.contrib import messages
from django.views.generic import *
from loginAPP.templates import *
from loginAPP.forms import *

class Index(TemplateView):
	template_name = 'login.html'

	def post(self,request,*args,**kwargs):
	
		if request.method == 'POST':
	
			form = LoginForm(request.POST)
			print(form.is_valid())
			if form.is_valid():
				username =  request.POST['username']
				password = request.POST['password']
				user_auth = authenticate_user(username, password)
				if user_auth is not None:
					if user_auth.is_active:
						user = authenticate(username=user_auth.username,
											password=password)
						
						if user:
							login(request, user)
							return HttpResponseRedirect(
								reverse_lazy('home'))
						else:
							messages.error(request,"Lo sentimos, su correo o contraseña no son correctos")
							return render(request,'login.html',
									  {'form': form})
							
					else:
						messages.error(request, "Aún no has confirmado tu correo.")
						return render(request,'login.html',
									  {'form': form})
				else:
					
					messages.error(request, "Lo sentimos, su correo o contraseña no son correctos.")
					return render(request,'login.html',
									  {'form': form})
			else:
				context = {'form': form}
				return render(request,'login.html', context)

		else:
			form = LoginForm()
		context = {'form': form, 'host': request.get_host()}
		return render(request,'login.html', context)



class Register(CreateView):

	model = User
	template_name = 'register.html'
	form_class = UserForm
	success_url = reverse_lazy('index')

class Home(TemplateView):
	template_name = 'home.html'


# Funcion que permite autenticar por username y correo
def authenticate_user(username=None, password=None):
	try:
		#Obtengo al usuario
		user = User.objects.get(username=username)
		if user is not None:
			return user
	except User.DoesNotExist:
		try:
			user = User.objects.get(email=username)
			if user is not None:
				return user
		except User.DoesNotExist:
			return None

class RestartPass(CreateView):
	template_name = 'RestartPass.html'