#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import *
from django.template import RequestContext
from django.views.generic import *
from login.forms import *

class Index(TemplateView):
    template_name = 'login.html'



    def post(self,request,*args,**kwargs):
        print("chaos")


        if request.method == 'POST':
            print("post")
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
                        print(user)
                        if user:
                            print("if user")
                            print(user)
                            login(request, user)
                            print("AQUI")
                            return HttpResponseRedirect(
                                reverse_lazy('home'))
                        else:
                            form.add_error(
                                None, "Su correo o contraseña no son correctos")
                    else:
                        form.add_error(None, "Aún no has confirmado tu correo.")
                        user = None
                else:
                    form.add_error(
                        None, "Su correo o contraseña no son correctos")
            else:
                context = {'form': form}
                return render_to_response('login.html', context,
                                          context_instance=RequestContext(request))

        else:
            form = LoginForm()
        context = {'form': form, 'host': request.get_host()}
        return render_to_response('login.html', context,
                                  context_instance=RequestContext(request))



class Register(CreateView):

    model = User
    template_name = 'register.html'
    form_class = UserForm
    success_url = reverse_lazy('index')


class Home(TemplateView):
    template_name = 'home.html'



def authenticate_user(username=None, password=None):
    print("holas")
    try:
        #Obtengo al usuario
        user = User.objects.get(username=username)
        print(user)
        if user is not None:
            print("no nose")
            return user
    except User.DoesNotExist:
        try:
            user = User.objects.get(email=username)
            print("hhhh ")
            if user is not None:
                return user
        except User.DoesNotExist:
            return None
