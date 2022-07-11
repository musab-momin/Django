from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Language, Framework
from .serializers import LanguageSerializer, FrameworkSerializer


# Create your views here.
@api_view(['GET'])
def index(request):
    all_language = Framework.objects.all()
    serializer = FrameworkSerializer(all_language, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def post_language(request):
    serializer = LanguageSerializer(data=request.data, many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def post_framework(request):
    data = request.data
    data['language'] = Language.objects.get(id = 1).id

    serializer = FrameworkSerializer(data=data, many=False)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
