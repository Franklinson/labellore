from rest_framework.serializers import ModelSerializer
from blog.models import Blogs, Category



class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blogs
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'