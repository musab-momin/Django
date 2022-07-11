from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Account


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Account        #specify which model is used for form creation
        fields = ('email', 'username', 'password') 

    #custom verlidation on email
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        
        try:
            account = Account.objects.get(email=email)
        except Exception as ex:
            return email

        raise forms.ValidationError(f'This {email} Email  is  already registered')

    #custom verlidation on username
    def clean_username(self):
        username = self.cleaned_data['username']
        
        try:
            account = Account.objects.get(username=username)
        except Exception as ex:
            return username

        raise forms.ValidationError(f'User already exists with this {username} username')




class UpdateAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email', 'username', 'profile_image', 'hide_email')

    #overiding save method
    def save(self, commit=True):
        account = super(UpdateAccountForm, self).save(commit=False)
        account.email = self.cleaned_data['email']
        account.username = self.cleaned_data['username']
        account.profile_image = self.cleaned_data['profile_image']   
        account.hide_email = self.cleaned_data['hide_email']


        if commit:
            account.save()
        return account