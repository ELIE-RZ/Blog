from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Postes

class FormUser(forms.ModelForm):
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)
    confirmPassword = forms.CharField(max_length=200, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirmPassword']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email = email).exists():
            raise ValidationError('Email incorrecte')
        return email
    def clean(self):
        clean_data= super().clean()
        password = clean_data['password']
        confirmPassword = clean_data['confirmPassword']
        if password and confirmPassword and password != confirmPassword:
            raise ValidationError('les mots de passe ne correspondent pas')
        return clean_data

class FormConnect (forms.Form):
    username = forms.CharField(max_length=200, widget=forms.TextInput)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)

class FormPost(forms.ModelForm):
    title = forms.CharField(max_length=300, widget=forms.TextInput)
    description = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Postes
        fields = ['title', 'description', 'picture']



class FormAdmin(forms.ModelForm):
    name_admin = forms.CharField(max_length=200, widget= forms.TextInput)
    email_admin = forms.CharField(max_length=200, widget= forms.EmailInput)
    password_admin = forms.CharField(max_length=200, widget=forms.PasswordInput)

class FormGroupe(forms.ModelForm):
    name_groupe = forms.CharField(max_length=200, widget=forms.TextInput)


