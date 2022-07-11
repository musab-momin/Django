from django.urls import path, include
from . import views;


app_name = 'DairyApi'
urlpatterns = [
    path('', views.dairy, name = 'ApiOverview'),
    path('add', views.add_to_dairy, name='AddToDairy'),
    path('single/<int:pk>', views.single_note, name='SingleNote'),
    path('remove/<int:pk>', views.remove_individual, name='Remove')
]