from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blog(request):
    return HttpResponse ('<h1> Here is a blog page </h1>')