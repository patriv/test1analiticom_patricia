#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
	passw = forms.CharField(label="Contraseña", required=True,
							widget=forms.PasswordInput())
	passw1 = forms.CharField(label="Repita Contraseña", required=True,
							widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ("username","email","first_name","last_name", )


		widgets = {
			'email': forms.TextInput(attrs={'required': 'true'}),
			'first_name': forms.TextInput(attrs={'required': 'true'}),
			'last_name': forms.TextInput(attrs={'required': 'true'})

		}

		labels = {
			'email': 'Correo',
			'first_name': 'Nombre',
			'last_name': 'Apellido',

			}

	def clean_username(self):
		username = self.cleaned_data.get('username')
		if User.objects.filter(username=username).count() != 0:
			raise forms.ValidationError(u'Este nombre de usuario ya está siendo utilizado.')
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email=email).count() != 0:
			raise forms.ValidationError(u'Este correo ya está siendo utilizado.')
		return email

	def clean(self):
		password1 = self.cleaned_data.get('passw')
		password2 = self.cleaned_data.get('passw1')
		lenPass = len(password1)

		if password1 and password1 != password2:
			msj = "Las contraseñas no coinciden, por favor intente nuevamente."
			self.add_error('passw1',msj)

		if (lenPass < 4) or (lenPass >= 8 ):
			msj = "La contraseña debe ser mayor a 4 dígitos y menor a 8."
			self.add_error('passw',msj)

		return self.cleaned_data

class LoginForm(forms.Form):

	class Meta:
		model = User
		fields = ('username','password','email',)
