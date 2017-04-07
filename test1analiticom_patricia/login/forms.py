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

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_active = 1
        password = self.cleaned_data['passw']
        password1 = self.cleaned_data['passw1']
        user.set_password(password)
        user.set_password(password1)
        user.save()
        return user

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

        if password1 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return self.cleaned_data

class LoginForm(forms.Form):

    class Meta:
        model = User
        fields = ('username','password','email',)
