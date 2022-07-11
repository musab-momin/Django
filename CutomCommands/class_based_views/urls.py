from django.urls import path, include
from . import views


app_name = 'ClassBasedView'
urlpatterns = [
    path('', views.IndexView.as_view(), name='IndexClassView'),
    path('parameter/<int:id>', views.Parameter.as_view(), name='ParameterClassView'),
    path('students/', views.StudentView.as_view(), name='StudentList'),
    path('student/<int:pk>', views.StudentDetailView.as_view(), name='DetailStudentView'),
    path('add_student/', views.AddStudentFormView.as_view(), name='AddStudnetView')
]
