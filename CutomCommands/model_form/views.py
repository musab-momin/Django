from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Computer
from .forms import ComputerRegisterForm


# Create your views here.
class ModelFormIndex(View):
    def get(self, request):
        context = {
            'title' : 'Model Form',
            'form' : ComputerRegisterForm()
        }
        return render(request, 'model_form/index.html', context)
    
    def post(self, request):
        form = ComputerRegisterForm(request.POST)
        if form.is_valid():
            print(f'''
                Brand : {form.cleaned_data['brand']}
                Name  : {form.cleaned_data['name']}
                Price : {form.cleaned_data['price']}
            ''')
            new_entry = Computer(name=form.cleaned_data['name'], brand=form.cleaned_data['brand'], price=form.cleaned_data['price'])
            new_entry.save()
        return redirect("/model_form/")


class ListOfComputer(ListView):
    model = Computer
    context_object_name = 'computers'