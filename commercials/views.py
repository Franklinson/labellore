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

# API to call individual blogs
# @api_view(['GET'])
# def blog(request, pk):
#     blog = Blogs.objects.get(id=pk)
#     serializer = BlogSerializer(blog, many=False)
#     return Response(serializer.data, status=status.HTTP_200_OK)