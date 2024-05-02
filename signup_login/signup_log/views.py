from django.shortcuts import render
from .models import UserCreds
from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

# Create your views here.

def register(request):
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


def login(request):
    if request.method == 'POST':
        mail = request.POST['email']