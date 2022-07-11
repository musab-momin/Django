from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('/post-language', views.post_language, name='PostLanguage'),
    path('/post-framework', views.post_framework, name='PostFramework')
]