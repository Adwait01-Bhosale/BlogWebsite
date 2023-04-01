from django.shortcuts import render, redirect
from datetime import datetime
from home.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from utils.decorator import login_required_message
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

class my_dictionary(dict):
 
  # __init__ function
  def __init__(self):
    self = dict()
 
  # Function to add key:value
  def add(self, key, value):
    self[key] = value

@login_required
def newblog(request):
    
    if request.method == "POST":
        print("entered in IF")
        # author_name = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        # print(author_name, title, content, datetime.today())
        user=request.user
        ins=BlogData(author=user.fullname,title=title, content=content, created_at=datetime.today(), user=request.user)
        ins.save()
        # print("Data Saved!!!")
    
    return render(request, 'newblog.html')

def home(request):
    
    if request.method=="POST":
        print("Entered in IF!!!!!")
        
        # contact_name=request.POST['contact_name']
        contact_email=request.POST['contact_email']
        contact_number=request.POST['contact_number']
        contact_subject=request.POST['contact_subject']
        contact_message=request.POST['contact_message']

        print(contact_email, contact_number, contact_subject, contact_message)
        user=request.user
        cont=ContactDetailsData(name=request.user, email=contact_email, number=contact_number, subject=contact_subject, message=contact_message, user=user)
        cont.save()
        return redirect('home')
    
    users = Account.objects.filter(is_admin=False).values('fullname', 'id')
    users = list(users)
    
    for user in users:
        if request.user.is_authenticated:
            content_data = BlogData.objects.filter(user=request.user).values_list('content')
            # print(request.user)
            context_blog_data=[]
            for i in range (len(content_data)):
                context_blog_data.append(content_data[i])
            
            print(len(context_blog_data))
            title_data = BlogData.objects.values_list('title')
            context_blog_title=[]
            
            for i in range (len(title_data)):
                context_blog_title.append(title_data[i])
            
            blog_title_dict=my_dictionary()            
            
            
            user['show'] = True            

            for i in range(len(context_blog_data)):
                blog_title_dict.add(context_blog_title[i][0], context_blog_data[i][0])
            
            print(len(blog_title_dict))
            print(blog_title_dict)
           
            
            return render(request, 'home.html', context={'blog_data':blog_title_dict,
                                                         'admin':request.user})
        else:
            user['show'] = False
            user['content'] = "Add some Content for the blog!"
    
    if request.user.is_authenticated:
        print("Logged in!!")
        mydata = BlogData.objects.filter(user=request.user).values()
        print(mydata)
    else:
        print("Not logged in!")
        
    return render(request, 'home.html')


def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })
    
    
def myblogs(request):
    return render(request,"myblogs.html")