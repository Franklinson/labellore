from rest_framework import serializers
from commercials.models import *


# Commeercial Food API
class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'


class NutrientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutrient
        fields = ['id', 'name']
        
        
class NutrientContentSerializer(serializers.ModelSerializer):
    content = ContentSerializer()
    unit = UnitSerializer()
    
    class Meta:
        model = NutrientContent
        fields = ['content', 'amount', 'unit']

class FoodNutrientSerializer(serializers.ModelSerializer):
    nutrient = NutrientSerializer()
    unit = UnitSerializer()

    class Meta:
        model = FoodNutrient
        fields = ['nutrient', 'amount', 'unit']

class FoodSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    nutrients = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()

    class Meta:
        model = Food
        fields = ['id', 'categories', 'name', 'brand', 'nutrients', 'content']

    def get_content(self, obj):
        food_contents = NutrientContent.objects.filter(food=obj)
        return NutrientContentSerializer(food_contents, many=True).data
    
    def get_nutrients(self, obj):
        food_nutrients = FoodNutrient.objects.filter(food=obj)
        return FoodNutrientSerializer(food_nutrients, many=True).data
