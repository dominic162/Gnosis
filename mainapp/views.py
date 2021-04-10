from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, FileResponse, Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import login_form , signup_form , ask_doubt , new_book
from .models import doubts, appuser, solution , book
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    context = {}
    return render(request, 'home.html', context)

def auth_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    
    context = {}

    if request.method == "POST":
        form = login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password']
            user = authenticate( username = username , password = password )
            if user:
                login(request,user)
                return HttpResponseRedirect("/")
            else:
                context['error'] = "Invalid username or password."
        else:
            context['error'] = "Username length must be 4-15 characters. Password length must be 8-16 characters"

    return render(request,'login.html',context)

def auth_signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    
    context = {
        'form':signup_form(),
    }

    if request.method == "POST":
        request.POST = request.POST.copy()
        request.POST['slug'] = slugify(request.POST['username'])
        form = signup_form( request.POST , request.FILES )
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            cnfpassword = request.POST['confirm_password']
            if password == cnfpassword:
                try:
                    user = User.objects.get( username = username )
                    context['error'] = 'User already exist. Try a different username'
                except:
                    user = User.objects.create_user( username = username, password = password )
                    login(request,user)                   
                    form.save()
                    login(request,user)
                    return HttpResponseRedirect("/")
            else:
                context['error'] = "Password and confirm password doesn't match"
        else:
            context['error'] = 'Please fill all required fields.'


    return render(request,'signup.html',context)

def auth_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

def allques(request):
    objects = doubts.objects.all()
    context = {
        'objects':objects,
    }
    return render(request, 'all_ques.html', context)


@login_required(login_url='/login')
def ask(request):
    context = {
        'form' : ask_doubt()
    }

    if request.method == "POST":
        request.POST = request.POST.copy()
        request.POST['author'] = appuser.objects.get( username = request.user.username )
        form = ask_doubt( request.POST )
        if form.is_valid() :
            form.save()
            return HttpResponseRedirect("/")
        else:
            context['error'] = 'error'

    return render(request, 'ask.html', context)

def show_doubt(request , pk ):
    doubt = doubts.objects.get( pk = pk )
    context={
        'object' : doubt,
    }
    if request.method == "POST":
        request.POST = request.POST.copy()
        request.POST['question'] = doubt
        request.POST['author'] = appuser.objects.get( username = request.user.username )
        obj = solution(answer = request.POST['answer'],
                       question = request.POST['question'],
                       author = request.POST['author'] )
        obj.save()
    return render(request, 'show_doubt.html', context)

@login_required( login_url = '/login')
def add_book(request):
    context = {}

    if request.method == "POST":
        request.POST = request.POST.copy()
        request.POST['uploaded_by'] = appuser.objects.get( username = request.user.username )
        form = new_book( request.POST , request.FILES )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

        else:
            context['error'] = 'Enter all required fields'

    return render(request, 'add_book.html', context)

def all_books(request):
    context = {
        'object' : book.objects.all(),
    }
    return render(request, 'all_books.html', context)

def book_view( request , pk ):
    context = {
        'object' : book.objects.get(pk = pk),
    }
    return render(request, 'book_view.html', context)

def user_info(request , slug):
    return HttpResponse("user_info")
