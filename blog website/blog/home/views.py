from django.shortcuts import render, redirect
from datetime import datetime
from home.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from utils.decorator import login_required_message


# Create your views here.
@login_required
def index(request):    
    if request.method=="POST":
        print("Entered in IF!!!!!")
        
        # contact_name=request.POST['contact_name']
        contact_email=request.POST['contact_email']
        contact_number=request.POST['contact_number']
        contact_subject=request.POST['contact_subject']
        contact_message=request.POST['contact_message']

        print(contact_email, contact_number, contact_subject, contact_message)
                
        cont=ContactDetailsData(name=request.user.fullname, email=contact_email, number=contact_number, subject=contact_subject, message=contact_message, user=request.user)
        cont.save()
    users = Account.objects.filter(is_admin=False).values('fullname', 'id')
    users = list(users)
    for user in users:
        if request.user.is_authenticated:
            data = BlogData.objects.order_by('-submitted_on')[0]
            blog_data=data.content
            blog_title=data.title
            print(blog_data)
            user['show'] = True
            user['content'] = blog_data
            return render(request,'index.html', context={'blog_data':blog_data,
                                                         'blog_title':blog_title})
        else:
            user['show'] = False
            user['content'] = "Add some Content for the blog!"
    return render(request,'index.html')

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
            data = BlogData.objects.order_by('-submitted_on')[0]
            blog_data=data.content
            print(blog_data)
            blog_title=data.title
            context_blog_data=blog_data
            user['show'] = True
            user['content'] = blog_data
            return render(request, 'home.html', context={'blog_data':context_blog_data,
                                                         'blog_title':blog_title})
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