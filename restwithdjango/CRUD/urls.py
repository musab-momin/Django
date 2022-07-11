from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='Home'),
    path('/task-list', views.task_list, name='TaskList'),
    path('/task-detail/<int:id>', views.task_detail, name='TaskDetail'),
    path('/create-task', views.create_task, name='CreateTask'),
    path('/update-task/<int:pk>', views.update_task, name='UpdateTask'), 
    path('/delete-task/<int:pk>', views.delete_task, name='DeleteTask')
]