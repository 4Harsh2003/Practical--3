from django.shortcuts import render
from django.http import HttpResponse

def stream(request):
    html="<html><body><h1>Select your stream </h1> <ol><li><a href=''>Management</a></li><li><a href=''>Legal</a><li><a href='course'>Computers</a></li></ol></body><html>"
    return HttpResponse(html)

def course(request):
    html="<html><body><h1>Select your course </h1> <ol><li><a href='year'>BCA</a></li><li><a href='year'>MCA</a></li></ol></body><html>"
    return HttpResponse(html)

def year(request):
    html="<html><body><h1>Select your Year </h1> <ol><li><a href='sem'>1st year</a></li><li><a href='sem'>2nd year</a></li><li><a href='sem'>3nd year</a></li></ol></body><html>"
    return HttpResponse(html)