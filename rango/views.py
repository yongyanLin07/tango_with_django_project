from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

def index(request): 
    url = "<a href='/rango/about'>About</a>"
    return HttpResponse("Rango says hey there partner!"+url)

def about(request):
    url = "<a href='/rango/'>Index</a>"
    return HttpResponse("HttpResponse:'Rango says here is the about page.' "+url)
