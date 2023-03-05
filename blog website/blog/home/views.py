from django.shortcuts import render, redirect
from datetime import datetime
from .models import Data, ContactDetails
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from utils.decorator import login_required_message


# Create your views here.
@login_required
def index(request):    
    if request.method=="POST":
        # print("Entered in IF!!!!!")
        
        contact_name=request.POST['contact_name']
        contact_email=request.POST['contact_email']
        contact_number=request.POST['contact_number']
        contact_subject=request.POST['contact_subject']
        contact_message=request.POST['contact_message']

        print(contact_name, contact_email, contact_number, contact_subject, contact_message)
                
        cont=ContactDetails(name=contact_name, email=contact_email, number=contact_number, subject=contact_subject, message=contact_message)
        cont.save()
    return render(request,'index.html')

@login_required_message(message="Please login, inorder to view the page")
@login_required
def newblog(request):
        
    if request.method == "POST":
        print("entered in IF")
        author_name = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        print(author_name, title, content, datetime.today())
        ins=Data(author=author_name, title=title, content=content, created_at=datetime.today())
        ins.save()
        # print("Data Saved!!!")
    return render(request, 'newblog.html')

def home(request):
    return render(request, 'home.html')

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
            messages.success(request, "You have logged in successfully!")
            return redirect('index')
        else:
            print("User Is Not Authenticated!!")
            messages.error(request, "Wrong Credentials!")
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
        
        if User.objects.filter(username=username):
            messages.error(request, "User already exists!!")
            return redirect('signup')
        
        if User.objects.filter(email=useremail):
            messages.error(request, "Email already exists!")
            return redirect('signup')
        
        if len(username)>10:
            messages.error(request, "Username must be below 10 characters")
            return redirect('signup')

        if pass1!=pass2:
            messages.error(request, "Passwords din't match!")
            return redirect('signup')
        
        print("Checkkk!!")
        myuser=User.objects.create_user(username, useremail, pass1)
        myuser.first_name=firstname
        myuser.last_name=lastname
        myuser.save()
        
        print("User Created Successfully!!")
        messages.success(request, "Your account has been successfully created!!")
        
        return redirect('login')
    return render(request, "signup.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out Successfully!!")
    return redirect('signup')