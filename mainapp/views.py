from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import loginform , signupform

# Create your views here.

def home(request):
    return HttpResponse('home')

def auth_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    
    context={}

    if request.method == "POST":
        form=loginform(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username , password=password)
            if user:
                login(request,user)
                return HttpResponseRedirect("/")
            else:
                context['error']="No user exist"
        else:
            context['error']="Username length must be 4-15 characters. Password length must be 8-16 characters"

    return render(request,'login.html',context)

def auth_signup(request):
    return render(request,'signup.html',context)

def auth_logout(request):
    logout(request)
    return HttpResponseRedirect("/")