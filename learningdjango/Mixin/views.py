from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import mixins
from rest_framework import generics


# Create your views here.
def index(request):
    return HttpResponse('This is working..')