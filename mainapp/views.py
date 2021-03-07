from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import loginform , signupform
from django.template.defaultfilters import slugify

# Create your views here.

def home(request):
    context={}
    return render(request, 'home.html', context)

def auth_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    
    context={}

    if request.method == "POST":
        form=loginform(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username'].lower()
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
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    
    context={
        'form':signupform(),
    }

    if request.method == "POST":
        data=request.POST.copy()
        data['slug']=slugify(data['username'])
        form=signupform(data)
        if form.is_valid():
            username=data['username']
            password=data['password']
            cnfpassword=data['confirm_password']
            if password == cnfpassword:
                try:
                    user=User.objects.get(username = username)
                    context['error']='User already exist. Try a different username'
                except:
                    user=User.objects.create_user(username = username, password = password)
                    login(request,user)                   
                    form.save()
                    login(request,user)
                    return HttpResponseRedirect("/")
            else:
                context['error'] = "Password and confirm password doesn't match"
        else:
            context['error']='Please fill all required fields.'


    return render(request,'signup.html',context)

def auth_logout(request):
    logout(request)
    return HttpResponseRedirect("/")