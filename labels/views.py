from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def home(request):
    context = {}
    return render(request, 'labels/home.html', context)


def label_list(request):
    # Query all labels from the database
    labels = Label.objects.all()
    
    # Pass the labels to the template
    return render(request, 'labels/viewnutrient.html', {'labels': labels})