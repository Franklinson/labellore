from rest_framework.serializers import ModelSerializer
from blog.models import Blogs, Category
from commercials.models import Label



class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blogs
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        

class LabelSerializer(ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'