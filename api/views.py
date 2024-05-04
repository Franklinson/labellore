from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import Blogs
from rest_framework import status

from .serializers import BlogSerializer
# Create your views here.

@api_view(['GET'])
def getfood(request):
    food =[
    {
        "brand": "null",
        "category": "OILS",
        "id": 13,
        "name": "Sunflower Oil",
        "nutrients": "Category:OILS ,Name:Sunflower Oil ,Brand:Bizee ,Net_Weight:1000.0 g,Serving_Size_Unit:None ,Per:100.0 ,Per_Unit:g ,Energy:900.0 Kcal,Fat:100.0 g,Saturated_Fat:11.7 g"
    },
    {
        "brand": "null",
        "category": "TINNED FOODS",
        "id": 24,
        "name": "Corned beef",
        "nutrients": "Category:TINNED FOODS ,Name:Corned beef ,Brand:Heinz ,Net_Weight:0.0 g,Serving_Size:0.0 ,Serving_Size_Unit:None ,Per:30.0 ,Per_Unit:None ,Energy:71.0 Kcal,Carbohydrate:0.3 g,Protein:6.6 g,Sugar:0.3 g,Fat:4.5 g,Saturated_Fat:2.5 g,Sodium:295.0 mg"
    },
    {
        "brand": "Afo",
        "category": "TINNED FOODS",
        "id": 27,
        "name": "Mackerel",
        "nutrients": "Category:TINNED FOODS ,Name:Mackerel ,Brand:Geisha ,Net_Weight:155.0 g,Serving_Size_Unit:None ,Per:60.0 ,Per_Unit:None ,Energy:90.0 Kcal,Protein:12.0 g,Fat:4.0 g,Saturated_Fat:2.5 g,Sodium:230.0 mg,Cholesterol:30.0 mg"
    },
    {
        "brand": "Ado",
        "category": "TINNED FOODS",
        "id": 28,
        "name": "Mackerel",
        "nutrients": "Category:TINNED FOODS ,Name:Mackerel ,Brand:Lele ,Net_Weight:150.0 g,Serving_Size_Unit:None ,Per:60.0 ,Per_Unit:None ,Energy:90.0 Kcal,Protein:12.0 g,Fat:4.0 g,Saturated_Fat:2.5 g,Sodium:230.0 mg,Cholesterol:30.0 mg"
    },
    {
        "brand": "Ama",
        "category": "TINNED FOODS",
        "id": 29,
        "name": "Mackerel",
        "nutrients": "Category:TINNED FOODS ,Name:Mackerel ,Brand:Sultana ,Serving_Size_Unit:None ,Per:100.0 ,Per_Unit:None ,Energy:164.0 Kcal,Carbohydrate:3.7 g,Protein:10.6 g,Sugar:1.5 g,Fat:11.8 g,Saturated_Fat:3.8 g,Sodium:456.0 mg"
    },
    {
        "brand": "Nutricia ",
        "category": "INFANT FORMULAE",
        "id": 30,
        "name": "Aptamil 1",
        "nutrients": "Category:INFANT FORMULAE ,Name:Aptamil 1 ,Brand:Nutricia  ,Serving_Size_Unit:g ,Per:100.0 ,Per_Unit:mls ,Saturated_Fat:1.5 g,Dietary_Fiber:0.6 g"
    },
    ]
    return Response(food)

# @api_view(['GET'])
# def news(request):
#     news = Blogs.objects.all()
#     serializer = BlogSerializer(news, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def postnews(request, pk):
#     news = Blogs.objects.get(id=pk)
#     serializer = BlogSerializer(news, many=False)
#     return Response(serializer.data, status=status.HTTP_200_OK)