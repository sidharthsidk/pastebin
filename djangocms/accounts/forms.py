from django.db.models.base import Model
from django.forms import forms, ModelForm,TextInput,PasswordInput
from django.forms import fields
from .models import User

class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['name','last_name', 'email', 'password'] 
        widgets = {
            'name':TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'last_name':TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email':TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'password':PasswordInput(
                attrs={
                    'class': 'form-control'
                }
            )
         
        } 