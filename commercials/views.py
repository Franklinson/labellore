from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from api.serializers import LabelSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


def home(request):
    context = {}
    return render(request, 'commercials/home.html', context)



# API to call all labels
@api_view(['GET'])
def labels(request):
    label = Label.objects.all()
    serializer = LabelSerializer(label, many=True)
    return Response(serializer.data)

# API to call individual food label
@api_view(['GET'])
def label(request, pk):
    onelabel = Label.objects.get(id=pk)
    serializer = LabelSerializer(onelabel, many=False)
    return Response(serializer.data)