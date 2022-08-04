from re import template
from django.urls import path
from django.views.generic import TemplateView
from classbasedviews import views


app_name = 'classbasedviews'
urlpatterns = [
    path('', TemplateView.as_view(template_name='classbasedviews/index.html'), name='Home'),
    path('about/', views.AboutUsView.as_view(), name='About'),
    path('baseview/', views.BaseView.as_view(template_name = 'classbasedviews/about.html'), name='BaseView'),
    path('detailview/<str:slug>', views.DetailViewOfBooks.as_view(), name='DetailView'),
    path('listview/', views.ListViewOfBooks.as_view(), name='ListView'),
    path('createview/', views.CreateViewOfBooks.as_view(), name='CreateView'),
    path('detailview/<str:slug>/updateview/', views.UpdateViewOfBooks.as_view(), name='UpdateView'),
    path('detailview/<str:slug>/delete/', views.DeleteViewOfBooks.as_view(), name='DeleteView')
]
