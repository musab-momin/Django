from django.urls import path, include
from . import views


app_name = 'NormalDairy'
urlpatterns = [
    path('', views.index, name = 'Home'),
    path('add', views.add_note, name = 'AddNote')
]