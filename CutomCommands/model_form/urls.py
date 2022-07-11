from django.urls import path, include
from . import views


app_name = 'ModelFormApp'

urlpatterns = [
    path('', views.ModelFormIndex.as_view(), name='ModelForm'),
    path('all/', views.ListOfComputer.as_view(), name='ListOfComputer')
]
