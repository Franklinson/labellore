from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import Blogs, Category
from rest_framework import status

from api.serializers import BlogSerializer, CategorySerializer


# API to call all blogs
@api_view(['GET'])
def blogs(request):
    blog = Blogs.objects.all()
    serializer = BlogSerializer(blog, many=True)
    return Response(serializer.data)

# API to call individual blogs
@api_view(['GET'])
def blog(request, pk):
    blog = Blogs.objects.get(id=pk)
    serializer = BlogSerializer(blog, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


# API to call all categories attached to blogs
@api_view(['GET'])
def categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


# API to call individual categories of a blog
@api_view(['GET'])
def category(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)