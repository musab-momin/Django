from .models import Computer
from django import forms
from django.core import validators


class ComputerRegisterForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ('brand', 'name', 'price')
        labels = {'brand' : 'Enter Brand Name', 'name': 'Enter Laptp Name', 'price' : 'Enter Price Name'}
        error_messages = {
            'brand': {'required':'Only 3 character are allowed'}
        }
        #to change input type of perticular field
        widgets = {
            'name' : forms.TextInput(attrs={'class':'inp'}),
            'brand': forms.TextInput(attrs={'placeholder' : 'e.g: Apple'}),
            'price' : forms.PasswordInput
        }