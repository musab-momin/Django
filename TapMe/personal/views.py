from django.shortcuts import render
from account.models import Account


# Create your views here.
def index(request):
    context = {
        'title':'TapMe',
        'is_loggedin' : False
    }
    if request.user.is_anonymous == False:
        account = Account.objects.get(email=request.user.email)
        context['active_user'] = account
        context['is_loggedin'] = True
    return render(request, 'personal/index.html', context)