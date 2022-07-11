from django.urls import path, include
from . import views



app_name = 'FormApi'
urlpatterns = [
    path('', views.IndexDjangoForm.as_view(), name='FormApiIndex'),
    path('all/', views.CarListView.as_view(), name='ListOfCarModel')
]