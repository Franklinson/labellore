from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def home(request):
    context = {}
    return render(request, 'labels/home.html', context)
