from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import LanguageSerializer, LanguageInventorSerializer, ProgrammerSerializer
from .models import Language, LanguageInventor, Programmer


# Create your views here.
class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (permissions.IsAuthenticated,)


class LanguageInventorView(viewsets.ModelViewSet):
    queryset = LanguageInventor.objects.all()
    serializer_class = LanguageInventorSerializer


class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer