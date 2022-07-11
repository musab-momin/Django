from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from rest_framework.request import Request


# Create your views here.

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': '/task-list/',
        'DetailView': '/task-detail/<int:pk>',
        'Create': '/task-create/',
        'Update': '/task-update/<int:pk>',
        'Delete': '/task-delete/<int:pk>'
    }
    return Response(['Welcome to Useless API', api_urls])


@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_detail(request, id):
    task = Task.objects.get(id = id)
    serlializer = TaskSerializer(task, many=False)
    return Response(serlializer.data)


@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response('501:Invalid Data')


@api_view(['POST'])
def update_task(request, pk):
    task = Task.objects.get(id = pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response('501:Invalid Data')


@api_view(['GET'])
def delete_task(request, pk):
    task = Task.objects.get(id = pk)
    task.delete()
    return Response('Item deleted successfully')