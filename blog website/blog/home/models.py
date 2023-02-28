from django.db import models
from froala_editor.fields import FroalaField

# Create your models here.


class Data(models.Model):
    author=models.CharField(max_length=1000, null=False)
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=10000)
    created_at=models.DateTimeField()
    def __str__(self):
        return self.title

class ContactDetails(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    number=models.IntegerField()
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=500)
    
    def __str__(self):
        return self.subject
