from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email =forms.EmailField(required=True)
    
    #family_key = forms.TextField(required=True)
    class Meta:
        model = User
        fields=("username","email")

    def save(self,commit=True):
        user=super(RegistrationForm,self).save(commit=False)
        #user.family_key=cleaned_data["family_key"]
        #user.email=cleaned_data["email"]
        if commit:
            user.save()
        return user