from django.shortcuts import render, redirect
from datetime import datetime
from .models import Data, ContactDetails
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.

def index(request):
    print("Hellosdfgb")
    # print(request.me)
    
    if request.method=="POST":
        print("Entered in IF!!!!!")
        
        contact_name=request.POST['contact_name']
        contact_email=request.POST['contact_email']
        contact_number=request.POST['contact_number']
        contact_subject=request.POST['contact_subject']
        contact_message=request.POST['contact_message']

        print(contact_name, contact_email, contact_number, contact_subject, contact_message)
                
        cont=ContactDetails(name=contact_name, email=contact_email, number=contact_number, subject=contact_subject, message=contact_message)
        cont.save()
    return render(request,'index.html')

def home2(request):
        
    if request.method == "POST":
        print("entered in IF")
        author_name = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        print(author_name, title, content, datetime.today())
        ins=Data(author=author_name, title=title, content=content, created_at=datetime.today())
        ins.save()
        print("Data Saved!!!")
        
    else:
        print("Hello")
    return render(request, 'newblog.html')


def Login(request):
    
    if request.method=="POST":
        
        data=request.POST
        
        username=data['login_username']
        email=data['login_email']
        password=data['login_pass']
        
        print(username, email, password)
        user=authenticate(username=username,password=password)
        
        print("User Is about to get Authenticated!!")
        
        if user is not None:
            print("User Is Authenticated!!")
            login(request, user)
            fname=user.first_name
            return render(request, "index.html", {'fname':fname})
        else:
            print("User Is Not Authenticated!!")
            messages.error(request, "Wrong Credentials")
            return redirect('login')
        
    return render(request, "login.html")

def signup(request):
    print("Entered Sign Up")
    if request.method=="POST":
        username=request.POST['signup_username']
        firstname=request.POST['signup_firstname']
        lastname=request.POST['signup_lastname']
        useremail=request.POST['signup_email']
        pass1=request.POST['signup_pass']
        pass2=request.POST['signup_pass2']

        myuser=User.objects.create_user(username, useremail, pass1)
        myuser.first_name=firstname
        myuser.last_name=lastname
        myuser.save()
        
        print("User Created Successfully!!")
        messages.success(request, "Your account has been successfully created!!")
        
        return redirect('login')
    return render(request, "signup.html")

def signout(request):
    pass