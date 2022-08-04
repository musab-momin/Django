from pyexpat import model
from turtle import width
from unicodedata import name
from attr import fields
from django import forms
from matplotlib import widgets
from djangoforms.models import Car


CHOICE_GENDER = [
    ('M', 'Male'),
    ('F', 'Female'),
]


class SearchForm(forms.Form):
    q = forms.CharField(label='search')
    

class NormalForm(forms.Form):
    name    = forms.CharField(label='Enter your name')
    email   = forms.CharField(label='Enter your email')
    phone   = forms.CharField(label='Enter your phone')
    age     = forms.IntegerField(label='Enter your age')
    dob     = forms.DateField(label='Enter DOB', widget=forms.SelectDateWidget)
    gender  = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICE_GENDER))
    terms   = forms.BooleanField(label='Terms and Condition', initial=True) #inital attribute is for intial value for field
    
    #naming convention is write clean_ and then the field name which you want to validate
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if  age < 18:
            raise forms.ValidationError('You are not an adult')
        return age


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'company_name', 'price', 'release_date']
        
        
        widgets = {
            'release_date' : forms.SelectDateWidget
        }
        
        #to change the lable of form fields
        labels = {
            'name': 'Car Name',
        }
        
        #to change the error message of a field
        error_messages = {
            'name' : {
                'required' : 'Please provide name of a car'
            }
        }