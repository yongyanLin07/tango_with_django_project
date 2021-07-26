from django.shortcuts import render
from django.http import HttpResponse

def index(request): 
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    #chapter2 url = "<a href='/rango/about'>About</a>"
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    url = "<a href='/rango/'>Index</a>"
    return HttpResponse("HttpResponse:'Rango says here is the about page.' "+url)
