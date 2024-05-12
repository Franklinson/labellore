from rest_framework.serializers import ModelSerializer
from blog.models import Blogs, Category
from commercials.models import Label, Brand, Unit, Nutrient, NutrientList
from django.contrib.auth.models import User



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



class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        
class UnitSerializer(ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'net_weight_unit', 'serving_size_unit', 'serving_quantity_unit','per_unit', 'energy_unit']
        
class NutrientSerializer(ModelSerializer):
    class Meta:
        model = Nutrient
        fields = '__all__'
        

class NutrientListSerializer(ModelSerializer):
    class Meta:
        model = NutrientList
        fields = '__all__'

class LabelSerializer(ModelSerializer):
    brand = BrandSerializer(read_only=True)
    unit = UnitSerializer(read_only=True)
    
    class Meta:
        model = Label
        fields = '__all__'