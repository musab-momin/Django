from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
    url = 'https://api.weatherapi.com/v1/current.json?key=c83cc7837ddc40c2aab62815220906&q={}&aqi=no'
    #city = 'Mumbai'
    context = {
        'city_weather': {}
    }
    if request.method == 'POST':
        city = request.POST.get('city')
        data = requests.get(url.format(city)).json()
        city_weather = {
            'city': city,
            'temp_cel': data['current']['temp_c'],
            'temp_fer': data['current']['temp_f'],
            'condition': data['current']['condition']['text'],
            'icon' : data['current']['condition']['icon']
        }
        context['city_weather'] = city_weather
    return render(request, 'index.html', context)