from pyexpat import model
from django.db import models

# Create your models here.


class post(models.Model):
    url = models.URLField(max_length=1000, unique=True)
    posted = models.BooleanField(default=False)
    released = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



class brand(models.Model):
    name=models.CharField(max_length=200,unique=True)
    brandurl = models.URLField(max_length=1000, unique=True, default="https://test.com")
    lastpost=models.URLField(max_length=1000,default="https://test.com")
    count=models.IntegerField(default=0)
    havenewpost = models.BooleanField(default=True)
    totalpost=models.IntegerField(default=-1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

