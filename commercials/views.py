from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Food
from .serializers import FoodSerializer

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes


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