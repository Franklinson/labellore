from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from blog.models import Blogs, Category
from commercials.models import Food, Brand, Unit, Nutrient, FoodNutrient
from django.contrib.auth.models import User


# Blog API
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BlogSerializer(ModelSerializer):
    author = UserSerializer(read_only=True)
    categories = CategorySerializer(read_only=True)
    class Meta:
        model = Blogs
        fields = '__all__'


# Commeercial Food API
class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class NutrientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutrient
        fields = ['id', 'name']

class FoodNutrientSerializer(serializers.ModelSerializer):
    nutrient = NutrientSerializer()
    unit = UnitSerializer()

    class Meta:
        model = FoodNutrient
        fields = ['nutrient', 'amount', 'unit']

class FoodSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    nutrients = serializers.SerializerMethodField()

    class Meta:
        model = Food
        fields = ['id', 'name', 'brand', 'nutrients']

    def get_nutrients(self, obj):
        food_nutrients = FoodNutrient.objects.filter(food=obj)
        return FoodNutrientSerializer(food_nutrients, many=True).data