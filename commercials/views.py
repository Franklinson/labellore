from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Food
from .serializers import FoodSerializer
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes


# from django_elasticsearch_dsl_drf.filter_backends import (
#     FilteringFilterBackend,
#     OrderingFilterBackend,
#     DefaultOrderingFilterBackend,
#     CompoundSearchFilterBackend,
# )
# from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
# from .documents import FoodDocument



def home(request):
    context = {}
    return render(request, 'commercials/home.html', context)




@api_view(['GET'])
@permission_classes([AllowAny])
def food_detail(request, pk):
    try:
        food = Food.objects.get(pk=pk)
    except Food.DoesNotExist:
        return Response({'error': 'Food not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = FoodSerializer(food)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def foods(request):
    try:
        foods = Food.objects.all()
    except Food.DoesNotExist:
        return Response({'error': 'Food not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = FoodSerializer(foods, many=True)
    return Response(serializer.data)




# class FoodDocumentView(DocumentViewSet):
#     permission_classes = [AllowAny]
#     document = FoodDocument
#     serializer_class = FoodSerializer
#     filter_backends = [
#         FilteringFilterBackend,
#         OrderingFilterBackend,
#         DefaultOrderingFilterBackend,
#         CompoundSearchFilterBackend,
#     ]

#     # Define search fields
#     search_fields = (
#         'name',
#         'categories',
#         'brand.brand',
#         'nutrients.name',
#         'content.content',
#     )

#     # Define filter fields
#     filter_fields = {
#         'categories': 'categories.raw',
#         'brand': 'brand.brand.raw',
#     }

#     # Define ordering fields
#     ordering_fields = {
#         'name': 'name.raw',
#         'categories': 'categories.raw',
#     }

#     # Default ordering
#     ordering = ('name',)

# class FoodDocumentView(DocumentViewSet):
#     permission_classes = [AllowAny]
#     document = FoodDocument
#     serializer_class = FoodSerializer

#     # Set the pagination class from `django_elasticsearch_dsl_drf`
#     pagination_class = PageNumberPagination

#     filter_backends = [
#         FilteringFilterBackend,
#         OrderingFilterBackend,
#         DefaultOrderingFilterBackend,
#         CompoundSearchFilterBackend,
#     ]

#     # Define search fields
#     search_fields = [
#         'name', 'categories'
#     ]

#     # Define filter fields
#     filter_fields = {
#         'categories': 'categories.keyword',
#         'brand': 'brand.brand.raw',
#         'nutrients': 'nutrients.name.raw',
#         'content': 'content.content.raw',
#     }

#     # Define ordering fields
#     ordering_fields = {
#         'name': 'name.keyword',
#         'categories': 'categories.keyword',
#     }

#     # Default ordering
#     ordering = ('name.keyword',)

#     def list(self, request, *args, **kwargs):
#         search_query = request.GET.get('name')
#         if search_query:
#             # Use the document class to perform a search with the query
#             search = self.document.search().query("match", name=search_query)
#             # Modify the queryset returned by the view
#             queryset = search.to_queryset()
#             page = self.paginate_queryset(queryset)
#             if page is not None:
#                 return self.get_paginated_response(page)
        
#         return super().list(request, *args, **kwargs)

# from django.shortcuts import render
from elasticsearch_dsl.query import MultiMatch
from .documents import FoodDocument
@api_view(['GET'])
@permission_classes([AllowAny])
def search_food(request):
    q = request.GET.get("q")
    results = []
    if q:
        query = MultiMatch(
            query=q, 
            fields=[
                "categories", 
                "name", 
                "brand.brand",  # Nested brand field
                "nutrients.unit.abbreviation",  # Nested unit abbreviation field for nutrients
                "content.unit.abbreviation",  # Nested unit abbreviation field for content
            ], 
            fuzziness="AUTO"
        )
        s = FoodDocument.search().query(query)[0:5]
        results = s.execute().to_dict()['hits']['hits']
    
    return Response({"foods": results})