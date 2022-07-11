from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ApiNote
from .serializers import ApiNoteSerializer
from rest_framework import status



# Create your views here.
@api_view(['GET'])
def dairy(request):
    all_notes = ApiNote.objects.all().order_by('-id')
    serializer = ApiNoteSerializer(all_notes, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
def add_to_dairy(request):
    if request.method == 'POST':
        serializer = ApiNoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'status_code':501, 'message': 'Internal Server Error'})
    
    return Response(['Make post request to api'])

@api_view(['GET'])
def single_note(request, pk):
    try:
        print(pk)
        single_note = ApiNote.objects.filter(id = pk).first()
        serializer = ApiNoteSerializer(single_note, many=False)
        return Response(serializer.data)
    except Exception as ex:
        print(ex)
        return Response({'status_code':402, 'message':'Record not found'})


@api_view(['GET'])
def remove_individual(request, pk):
    try:
        single_note = ApiNote.objects.filter(id = pk).first()
        single_note.delete()
        return Response({'status_code':200, 'message':'Record deleted successfully'})
    except Exception as ex:
        print(ex)
        return Response({'status_code':402, 'message':'Record not found'})

