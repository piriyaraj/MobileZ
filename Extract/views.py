from http.client import HTTPResponse
import re
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from . import tools
# Create your views here.
def index(request):
    tools.test()
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def newpostcheck(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
