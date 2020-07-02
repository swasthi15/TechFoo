import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.conf import settings
import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth
import time

def signup(request):
	print("signup")
	return render(request,'signup1.html')

def signup_submit(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    print(username)
    print(password,email)
    user = User.objects.create_user(username, email,password)
    user.save()

    return redirect('/login')

	
def login(request):
	print(request.user)
	return render(request,'login.html')

def logging_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    print(user)
    print("login")
    if user is not None:
        auth.login(request,user)
        print("Successfull")

        print(username)
        return redirect('/')
        # Redirect to a success page.
        ...
    else:
        return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')


def index(request):
	print(type(request.user))

	print("Hitting Home Page Successfull")

	if(request.user.is_authenticated)	:
		print(request.user)	
		return redirect('/location/')
	else:
		return redirect('/login/')



def access_location(request):

	return render(request,'location.html')

