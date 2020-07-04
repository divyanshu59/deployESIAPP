from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from user.models import User

def registerHome(request):
    return render(request,'registration/home.html')




   