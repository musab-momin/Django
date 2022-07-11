from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Car
from .forms import CarForm



# Create your views here.
class IndexDjangoForm(View):
    def get(self, request):
        car_frm = CarForm()
        context = {'title': 'Learning Forms Api', 'form': car_frm}
        return render(request, 'form_api/index.html', context)
    
    def post(self, request):
        form =  CarForm(request.POST)
        if form.is_valid():
            
            name = form.cleaned_data['name']
            brand = form.cleaned_data['brand']
            price = form.cleaned_data['price']

            print(f'''
                Name : {name}
                Brand : {brand}
                price : {price}
            ''')
           
        return redirect('/form_api/')


class CarListView(ListView):
    model = Car
    template_name = 'form_api/car_list.html'
    context_object_name = 'cars'



