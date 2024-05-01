from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
from .models import UserCreds
from django.http import JsonResponse 
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
=======
>>>>>>> 0e1be4d2f8d6cc81c1ae890b41b7f410249149cb

# Create your views here.

def index(request):
<<<<<<< HEAD
    if request.method == 'POST':
        mail = request.POST['email']
        user = request.POST['username']
        passw = request.POST['password']
        confirm = request.POST['conpass']
        
        new_user= UserCreds(email=mail, username=user, password=passw)
        new_user.save()
    return render(request,'index.html')


def check_username(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        print(username)
        exists = UserCreds.objects.filter(username=username).exists()
        return JsonResponse({'exists': exists})
=======
>>>>>>> 0e1be4d2f8d6cc81c1ae890b41b7f410249149cb
    return render(request,'index.html')
