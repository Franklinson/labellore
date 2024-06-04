from rest_framework.serializers import ModelSerializer
from blog.models import Blogs, Category
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