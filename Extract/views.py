from http.client import HTTPResponse
import re
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from . import tools
# Create your views here.
def index(request):
    tools.test()
    return render(request,'Extract/index.html')


def getNewPostFromWebsit(request):
    tools.checkForNewPost()
    return render(request, 'Extract/index.html')


def checkReleasedPostInDataBase(request):
    tools.databasePostReleased()
    return render(request, 'Extract/index.html')
