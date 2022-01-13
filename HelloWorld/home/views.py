from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    constext = {
        "mssg": "I just still this code",
        "logo": "Start Django"
    }
    return render(request, "index.html", constext)
