from django.urls import path
from djangoforms import views


app_name = 'DjangoForms'
urlpatterns = [
    path('searchform/', views.SearchFormView.as_view(), name='SearchForm'),
    path('normalform/', views.NormalFormView.as_view(), name='NormalForm'),
    path('modelform/', views.ModelFormView.as_view(), name='PostModelForm')
]
