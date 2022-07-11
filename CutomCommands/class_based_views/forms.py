from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=70)



class StudentForm(forms.Form):
    name    = forms.CharField(max_length=70)
    roll    = forms.IntegerField()
    course  = forms.CharField(max_length=70)

    