from django.db import models
from froala_editor.fields import FroalaField
from userauth.models import Account
from django.utils import timezone

# Create your models here.


class BlogData(models.Model):
    author=models.CharField(max_length=1000, null=True)
    title=models.CharField(max_length=100, null=True)
    content=models.CharField(max_length=10000, null=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True)
    submitted_on = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return str(self.user) + str(self.submitted_on.strftime(f" - [%d %B %Y]"))

class ContactDetailsData(models.Model):
    name=models.CharField(max_length=200, null=True)
    email=models.CharField(max_length=100, null=True)
    number=models.IntegerField(null=True)
    subject=models.CharField(max_length=100, null=True)
    message=models.CharField(max_length=500, null=True)
    submitted_on = models.DateTimeField(default=timezone.now)
    
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name + self.submitted_on.strftime(f" - [%d %B %Y]")
