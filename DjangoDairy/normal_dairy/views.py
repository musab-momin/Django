from django.shortcuts import render
from .models import Note
from django.contrib import messages


# Create your views here.
def index(request):
    all_notes = Note.objects.all()
    print(all_notes)
    context = {
        'title': 'Django | Dairy',
        'notes': all_notes
    }
    return render(request, 'index.html', context)


def add_note(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        try:
            Note.objects.create(content=content)
            messages.info(request, 'New note created succssfully')
        except Exception as ex:
            messages.info(request, 'Something went wrong')
            print(ex)
    context = {
        'title': 'Dairy | Add Note'
    }



    return render(request, 'add.html', context)
