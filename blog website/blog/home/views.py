from django.shortcuts import render
from datetime import datetime
from .models import Data, ContactDetails

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