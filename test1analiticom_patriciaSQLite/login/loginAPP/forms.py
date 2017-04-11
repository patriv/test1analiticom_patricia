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


	def clean_username(self):
		username = self.cleaned_data.get('username')
		if User.objects.filter(username=username).count() != 0:
			raise forms.ValidationError(u'Este nombre de usuario ya está siendo utilizado.')
		return username

	def clean_email(self):
		print("Clean email")
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

	def save(self, commit=True):
		user = super(UserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.username = self.cleaned_data['username']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.is_active = 1
		password = self.cleaned_data['passw']
		user.set_password(password)
		user.save()
		return user


class LoginForm(forms.Form):

	class Meta:
		model = User
		fields = ('username','password','email',)


class EmailForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ("email", )

		widgets = {
			'email': forms.EmailInput(attrs=
                                     {'required': 'true', 'placeholder':'Correo Electrónico'})
		}

	def clean(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email=email).count() == 0:
			msj = 'Este correo no está registrado, por favor, verifíquelo.'
			self.add_error('email', msj)
		return self.cleaned_data


class NewPasswForm(forms.Form):
	passw = forms.CharField(label="Contraseña", required=True,
							widget=forms.PasswordInput())
	passw1 = forms.CharField(label="Repita Contraseña", required=True,
							 widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ("passw","passw1",)

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


