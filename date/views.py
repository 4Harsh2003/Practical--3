from django.shortcuts import render
from django.http import HttpResponse
import datetime
def time(request):
    now=datetime.datetime.now()
    html="<html><body> <h1>It is now %s</h1></body></html>"% now #here i have doubt in syntax
    return HttpResponse(html)


