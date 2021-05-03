
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import login_form , signup_form , ask_doubt , new_book , contact_form , links_info
from .models import doubts, appuser, solution , book , extra_info
from taggit.models import Tag
from django.template.defaultfilters import slugify




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
    all_doubts = doubts.objects.all()
    all_tags = Tag.objects.all()
    pth_dbt = doubts.objects.filter(tags__slug = 'python')
    cvd = doubts.objects.filter(tags__slug = 'covid')
    tech = doubts.objects.filter(tags__slug = 'tech')
    webd_d = doubts.objects.filter(tags__slug = 'webd')
    politics = doubts.objects.filter(tags__slug = 'politics')

    context = {
        'doubts' : all_doubts,
        'alltags' : all_tags,
        'pthdbt' : pth_dbt,
        'webd' : webd_d,
        'tech' : tech,
        'covid' : cvd,
        'politics' : politics,

    }

    if request.user.is_authenticated:
        cuser = appuser.objects.filter(username = request.user.username).first()
        ydoubt = doubts.objects.filter(author = cuser)
        context['cuser'] = ydoubt


    if request.method == "POST":
        if 'search_query' in request.POST : 
            query = request.POST['search_query']
            post1 = doubts.objects.filter(question__icontains = query)
            post2 = doubts.objects.filter(tags__slug = query)
            allpost = post1.union(post2)
            context['allpost'] = allpost
            context['query'] = query
        
        if 'ask' in request.POST : 
            request.POST = request.POST.copy()
            request.POST['author'] = appuser.objects.get( username = request.user.username )
            form = ask_doubt( request.POST )
            if form.is_valid() :
                form.save()
            else:
                context['error'] = 'Enter all required fields'
            

    return render(request, 'all_ques.html', context)




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


def all_books(request):
    context = {
        'object' : book.objects.all(),
    }
    if request.method == "POST":
        if 'search_query' in request.POST:
            query = request.POST['search_query']
            post1 = book.objects.filter(name__icontains = query)
            post2 = book.objects.filter(tags__slug = query)
            allpost = post1.union(post2)
            context['allpost'] = allpost
            context['query'] = query
        
        if 'add_book' in request.POST:
            request.POST = request.POST.copy()
            request.POST['uploaded_by'] = appuser.objects.get( username = request.user.username )
            form = new_book( request.POST , request.FILES )
            if form.is_valid():
                form.save()
                context['success'] = 'New Book added successfully'
            else:
                context['error'] = 'Enter all required fields'
            
    return render(request, 'all_books.html', context)

def user_info(request , slug):
    
    context = {
        'object' : appuser.objects.get(slug = slug)
    }
    if request.method == "POST":
        request.POST = request.POST.copy()
        
        cuser = appuser.objects.get( username = request.user.username )
        cinst = extra_info.objects.filter( author = cuser )
        if cinst:
            cinst = extra_info.objects.get( author = cuser )
            if request.POST['bio']:
                cinst.bio = request.POST['bio']
            if request.POST['site_link']:
                cinst.site_link = request.POST['site_link']
            if request.POST['gthb_link']:
                cinst.gthb_link = request.POST['gthb_link']
            if request.POST['twtr_link']:
                cinst.twtr_link = request.POST['twtr_link']
            if request.POST['inst_link']:
                cinst.inst_link = request.POST['inst_link']
            if request.POST['fb_link']:
                cinst.fb_link = request.POST['fb_link']
            
            cinst.save()
            context['success'] = "'Successfully updated'"
            
        else:
            request.POST['author'] = cuser
            cinst = links_info(request.POST)
            if cinst.is_valid():
                cinst.save()
                context['success'] = 'Successfully updated'
            else:
                context['error'] = 'Enter all fields correctly'
    return render(request , 'user.html', context)


def contact_us(request):
    context = { }
    if request.method == 'POST':
        form = contact_form( request.POST )
        if form.is_valid():
            form.save()
            context['success'] = 'Message sent successfully'
        else:
            context['error'] = 'Enter all required fields correctly.'

    return render(request , 'contact.html' , context)

